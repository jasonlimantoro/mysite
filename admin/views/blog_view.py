from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from polls.models import Blog
from ..forms import BlogForm, CommentForm


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'admin/blogs/index.html', {
        'blogs': blogs,
    })


@require_http_methods(['POST'])
def store(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        Blog.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            category=form.cleaned_data['category'],
            user=request.user
        )
        messages.success(request, "A blog is successfully created")
    else:
        messages.error(request, "Form is invalid")
        return render(request, 'admin/blogs/create.html', {'form': form})

    return HttpResponseRedirect(reverse('admin:blogs.index'))


def create(request):
    form = BlogForm()
    return render(request, 'admin/blogs/create.html', {'form': form})


def show(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = CommentForm()
    return render(request, 'admin/blogs/show.html', {
        'blog': blog,
        'form': form,
    })


def edit(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    form = BlogForm(initial={
        'title': blog.title,
        'description': blog.description,
        'category': blog.category,
    })
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
        return render(request, 'admin/blogs/edit.html', {'blog': blog, 'form': form })

    return HttpResponseRedirect(reverse('admin:blogs.edit', args=(blog_id, )))


@require_http_methods(['POST'])
def destroy(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog is successfully deleted')
    return HttpResponseRedirect(reverse('admin:blogs.index'))
