from django import forms
from .models import Comment, Author

class RegistrationForm(forms.Form):
    username = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField()
    repeat_password = forms.CharField()
    

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')