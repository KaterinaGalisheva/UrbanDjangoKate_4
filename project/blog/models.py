from django.db import models
from django.urls import reverse
from django.utils import timezone # часовые пояса
from taggit.managers import TaggableManager


# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)  
    username = models.CharField(max_length=15, unique=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=128) 
    
    def __str__(self):
        return self.username
    


class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(max_length=2000)
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, 
                                                 self.publish.month, self.publish.day, self.slug])


    class Meta: # порядок сортировки статей
        ordering = ('-publish',)
    def __str__(self):
        return self.title 



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    

