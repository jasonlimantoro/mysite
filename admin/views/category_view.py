from django.shortcuts import render
from polls.models import Category


def index(request):
    categories = Category.objects.all()
    return render(request, 'admin/categories/index.html', {
        'categories': categories,
    })


def show(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'admin/categories/show.html', {
        'category': category,
    })


def edit(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'admin/categories/edit.html', {
        'category': category,
    })

