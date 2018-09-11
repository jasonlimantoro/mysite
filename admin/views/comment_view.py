from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.contrib import messages
from polls.models import Blog, Comment
from ..forms import BlogForm, CommentForm


def edit(request, blog_id, comment_id):
    blog = Blog.objects.get(pk=blog_id)
    comment = Comment.objects.get(pk=comment_id)
    form = CommentForm(initial={
        'content': comment.content
    })
    return render(request, 'admin/comments/edit.html', {
        'blog': blog,
        'comment': comment,
        'form': form
    })


@require_http_methods(['POST'])
def store(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        blog.comments.create(
            content=form.cleaned_data['content'],
            user=request.user
        )
        messages.success(request, 'Comment is successfully attached to this blog')

    else:
        messages.error(request, "Form is not valid")

    return redirect('admin:blogs.show', blog_id)


@require_http_methods(['POST'])
def update(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment.content = form.cleaned_data['content']
        comment.save()
        messages.success(request, 'Comment is successfully updated')

    else:
        messages.error(request, 'Form is invalid')

    return HttpResponseRedirect(reverse('admin:blogs.show', args=(comment.blog_id, )))


@require_http_methods(['POST'])
def destroy(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)

    comment.delete()

    messages.success(request, 'Comment is deleted successfully!')

    return HttpResponseRedirect(reverse('admin:blogs.show', args=(comment.blog_id,)))
