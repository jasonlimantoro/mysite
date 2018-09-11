from django import forms
from django.forms import Select
from polls.models import Blog, Comment


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
