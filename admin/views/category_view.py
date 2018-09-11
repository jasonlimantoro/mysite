from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from polls.models import Category


def index(request):
    categories = Category.objects.all()
    user = request.user
    return render(request, 'admin/categories/index.html', {
        'categories': categories,
        'user': user,
    })

def show(request, category_id):
    category = Category.objects.get(pk=category_id)
    user = request.user
    return render(request, 'admin/categories/show.html', {
        'category': category,
        'user': user,
    })

def edit(request, category_id):
    category = Category.objects.get(pk=category_id)
    user = request.user
    return render(request, 'admin/categories/edit.html', {
        'category': category,
        'user': user,
    })

