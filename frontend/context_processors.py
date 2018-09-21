from frontend.models import Category
from django.contrib.auth.forms import AuthenticationForm


def categories(request):
    return {'categories': Category.objects.all()}


def login_form(request):
    return {'login_form': AuthenticationForm()}
