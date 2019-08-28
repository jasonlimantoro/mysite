from functools import wraps
from frontend.models import Blog, Comment
from django.contrib import messages
from django.shortcuts import redirect, reverse


def blog_owner_required(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        blog = Blog.objects.get(pk=kwargs['blog_id'])
        if blog.user != request.user:
            messages.error(request, 'Only author is allowed to edit this blog')
            return redirect(reverse('admin:blogs.index'))
        return func(request, *args, **kwargs)

    return wrap


def comment_owner_required(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['comment_id'])
        if comment.user != request.user:
            messages.error(
                request,
                'Only comment author is allowed to perform this operation')
            return redirect(reverse('admin:blogs.index'))
        return func(request, *args, **kwargs)

    return wrap
