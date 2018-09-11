from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from polls.models import Blog
from ..forms import BlogForm


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'admin/blogs/index.html', {
        'blogs': blogs,
    })


def show(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'admin/blogs/show.html', {
        'blog': blog,
    })


def edit(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = BlogForm(initial={
        'title': blog.title,
        'description': blog.description,
        'category': blog.category,
    })
    # categories = Category.objects.all()
    return render(request, 'admin/blogs/edit.html', {
        'blog': blog,
        'form': form
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
        messages.error(request, "Form is not valid")
    return render(request, 'admin/blogs/edit.html', {
        'form': form,
        'blog': blog,
    })
