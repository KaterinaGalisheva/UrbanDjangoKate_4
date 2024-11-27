from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from taggit.models import Tag
from django.db.models import Count 
from .models import Post, Comment, Author
from .forms import EmailPostForm, CommentForm, RegistrationForm
from django.utils import timezone

# Create your views here.

# функция пагинатора для отображения статей
def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags=tag)

    try:
        items_per_page = int(request.GET.get('items_per_page', 4))
    except ValueError:
        items_per_page = 4  

    paginator = Paginator(object_list.order_by('id'), items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if not page.object_list:
        messages.info(request, 'No posts available')

    context = {
        'posts': page.object_list,  # Передаем только объекты текущей страницы
        'page': page,                # Передаем сам объект страницы
        'request': request,
        'tag': tag
    }
    
    return render(request, 'blog/list.html', context)



# отображение деталей поста
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm(initial={
        'name': request.user.username,  
        'email': request.user.email     
    }) 
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    post_tags_ibs = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ibs).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    context = {
        'post': post,
        'comments': comments, 
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts': similar_posts  
    }

    return render(request, 'blog/detail.html', context)


# функция отправки постов
def post_share(request, post_id):
    # получение статьи по id
    post = get_object_or_404(Post, id=post_id, status='published')
    form = EmailPostForm(initial={
        'name': request.user.username,  
        'email': request.user.email     
    })
    sent = False
    context = {
            'post': post,
            'form': form,
            'sent': sent
        }

    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            # отправка поста
            post_url = request.build_absolute_uri(post.get_absolute_url())  
            subject = f"{cd['name']} ({cd['email']}) recommends you reading '{post.title}'"
            message = f'Read "{post.title}" at {post_url}\n\n{cd["name"]}\'s comments:\n{cd["comments"]}' 
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
        else:
            form = EmailPostForm()
        
    return render(request, 'blog/share.html', context)


# функции для регистрации пользователей   
def sign_up(request):
    users = Author.objects.all()
    info = {}
    context = {
        'info':info,
        'users':users
     }
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            age = request.POST.get('age')
            email = request.POST.get('email')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'blog/registration.html', context)
            elif int(age) < 18:
                info['error'] = 'Вы несовершеннолетний'
                return render(request, 'blog/registration.html', context)
            elif Author.objects.filter(username=username).exists():
                info['error'] = 'Такой пользователь уже существует'
                return render(request, 'blog/registration.html', context)
            else:
                Author.objects.create(username=username, age=age, email=email, password=password)
                info['error'] = "Регистрация прошла успешно!"
                return render(request, 'blog/registration.html', context)
            
                
    else:
        form = RegistrationForm()  

    return render(request, 'blog/registration.html', context)