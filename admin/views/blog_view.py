from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from polls.models import Blog, Category
from ..forms import BlogForm


def index(request):
    blogs = Blog.objects.all()
    user = request.user
    return render(request, 'admin/blogs/index.html', {
        'blogs': blogs,
        'user': user,
    })


def show(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    user = request.user
    return render(request, 'admin/blogs/show.html', {
        'blog': blog,
        'user': user,
    })


def edit(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    user = request.user
    # form = BlogForm(initial={
    #     'title': blog.title,
    #     'description': blog.description,
    #     'category': blog.category,
    # })
    categories = Category.objects.all()
    return render(request, 'admin/blogs/edit.html', {
        'blog': blog,
        'user': user,
        'categories': categories,
        # 'form': form
    })


@require_http_methods(['POST'])
def update(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = BlogForm(request.POST)
    if form.is_valid():
        blog.title = form.cleaned_data['title']
        blog.description = form.cleaned_data['description']
        blog.category = form.cleaned_data['category']
        blog.save()
        messages.success(request, 'Blog is updated successfully!')
    else:
        raise ValidationError('invalid')

    return HttpResponseRedirect(reverse('admin:blogs.edit', args=(blog_id,)))
