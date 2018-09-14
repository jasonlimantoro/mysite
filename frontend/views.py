from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Blog, Category


def home(request):
    query = request.GET.get('query')
    blogs = Blog.objects.all()
    if query:
        blogs = blogs.filter(title__icontains=query)

    return render(request, 'frontend/home.html', {
        'blogs': blogs,
        'query': query,
    })


def show_category(request, id):
    category_to_show = Category.objects.get(pk=id)
    query = request.GET.get('query')
    blogs = category_to_show.blogs.all()
    if query:
        blogs = blogs.filter(title__icontains=query)

    return render(request, 'frontend/categories/show.html', {
        'category_to_show': category_to_show,
        'blogs': blogs,
        'query': query,
    })
