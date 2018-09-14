from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Blog, Category


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'frontend/home.html', {
        'blogs': blogs,
    })


def show_category(request, id):
    category_to_show = Category.objects.get(pk=id)
    return render(request, 'frontend/categories/show.html', {
        'category_to_show': category_to_show,
    })
