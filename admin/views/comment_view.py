from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from frontend.models import Blog, Comment
from ..forms import CommentForm
from ..decorators import comment_owner_required


@login_required
@comment_owner_required
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


@login_required
@require_http_methods(['POST'])
def store(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        blog.comments.create(
            content=form.cleaned_data['content'],
            user=request.user
        )
        messages.success(
            request,
            'Comment is successfully attached to this blog')

    else:
        messages.error(request, "Form is not valid")

    return redirect('admin:blogs.show', blog_id)


@login_required
@comment_owner_required
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

    return HttpResponseRedirect(
        reverse(
            'admin:blogs.show',
            args=(
                comment.blog_id,
            )))


@login_required()
@comment_owner_required
def toggle_visibility(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.is_hidden = not comment.is_hidden
    comment.save()
    messages.success(request, "Comment visibility is successfully changed")

    return HttpResponseRedirect(
        reverse(
            'admin:users.show',
            args=(
                comment.user.id,
            )))


@login_required
@comment_owner_required
@require_http_methods(['POST'])
def destroy(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)

    comment.delete()

    messages.success(request, 'Comment is deleted successfully!')

    return HttpResponseRedirect(
        reverse(
            'admin:blogs.show',
            args=(
                comment.blog_id,
            )))
