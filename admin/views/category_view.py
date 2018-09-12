from django.shortcuts import render, reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from polls.models import Category
from ..forms import CategoryForm


@login_required
def index(request):
    categories = Category.objects.all()
    return render(request, 'admin/categories/index.html', {
        'categories': categories,
    })


@login_required
def create(request):
    form = CategoryForm()
    return render(request, 'admin/categories/create.html', {'form': form})


@login_required
@require_http_methods(['POST'])
def store(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        Category.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description']
        )
        messages.success(request, 'Category is successfully created')
    else:
        messages.error(request, 'Form is invalid')
        return render(request, 'admin/categories/create.html', {'form': form})

    return HttpResponseRedirect(reverse('admin:categories.index'))


@login_required
def show(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'admin/categories/show.html', {
        'category': category,
    })


@login_required
def edit(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(initial={
        'title': category.title,
        'description': category.description,
    })
    return render(request, 'admin/categories/edit.html', {
        'category': category,
        'form': form,
    })


@login_required
@require_http_methods(['POST'])
def update(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(request.POST)
    if form.is_valid():
        category.title = form.cleaned_data['title']
        category.description = form.cleaned_data['description']
        category.save()
        messages.success(request, 'Category is successfully created')
    else:
        messages.error(request, 'Form is invalid')
        return render(request, 'admin/categories/edit.html', {'form': form, 'category': category})

    return HttpResponseRedirect(reverse('admin:categories.edit', args=(category.id,)))


@login_required
def destroy(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    messages.success(request, 'Category is successfully deleted')
    return HttpResponseRedirect(reverse('admin:categories.index'))
