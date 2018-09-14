from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from polls.models import Blog, Category, Profile
from admin.forms import UserForm, CommentForm


def home(request):
    query = request.GET.get('query')
    blogs = Blog.objects.all()
    if query:
        blogs = blogs.filter(title__icontains=query)

    return render(request, 'frontend/home.html', {
        'blogs': blogs,
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
    })


def show_blog(request, id):
    blog = Blog.objects.get(pk=id)
    is_liked = blog.is_liked_by(request.user)
    form = CommentForm()
    return render(request, 'frontend/blogs/show.html', {
        'blog': blog,
        'is_liked': is_liked,
        'form': form,
    })


def register(request):
    form = UserForm()
    return render(request, 'frontend/pages/registration.html', {'form': form})


def signup(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        Profile.objects.create(user=user)
        login(request, user)
        messages.success(request, "Welcome to the administration board!")
    else:
        messages.error(request, "Form is invalid!")
        return render(request, 'frontend/pages/registration.html', {'form': form})

    return redirect('admin:index')
