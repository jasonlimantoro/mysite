from django import forms
from django.forms import Select, PasswordInput, EmailInput
from polls.models import Blog, Comment, Category
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category']
        widgets = {
            'category': Select(attrs={'class': 'ui search dropdown'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'email': EmailInput(attrs={'required': True}),
            'password': PasswordInput()
        }

