from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from polls.models import Blog, Category, Profile
from admin.forms import CommentForm


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
    form = UserCreationForm()
    return render(request, 'frontend/pages/registration.html', {'form': form})


def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        Profile.objects.create(user=user)
        login(request, user)
        messages.success(request, "Welcome to the administration board!")
    else:
        return render(request, 'frontend/pages/registration.html', {'form': form})

    return redirect('admin:index')


def login_view(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "You are logged in!")
        if 'next' in request.POST:
            redirect(request.POST.get('next'))
        return redirect('admin:index')

    return redirect('frontend:home')

