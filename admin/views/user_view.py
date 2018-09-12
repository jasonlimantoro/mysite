from django.shortcuts import render, reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from polls.models import User
from ..forms import UserForm


@login_required
def index(request):
    users = User.objects.all()
    return render(request, 'admin/users/index.html', {'users': users})


@login_required
@require_http_methods(['POST'])
def store(request):
    form = UserForm(request.POST)
    if form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        messages.success(request, "User is successfully created")

    else:
        messages.error(request, "Form is invalid")
        return render(request, 'admin/users/create.html', {'form': form})

    return HttpResponseRedirect(reverse('admin:users.index'))


@login_required
def create(request):
    form = UserForm()
    return render(request, 'admin/users/create.html', {'form': form})


@login_required
def show(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'admin/users/show.html', {'user': user})


@login_required
@require_http_methods(['POST'])
def toggle_ban(request, user_id):

    user = User.objects.get(pk=user_id)
    user.is_active = not user.is_active
    user.save()

    messages.success(request, "User status is successfully changed")

    return HttpResponseRedirect(reverse('admin:users.index'))
