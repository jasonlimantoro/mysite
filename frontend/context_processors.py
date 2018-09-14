from polls.models import Category
from admin.forms import UserForm


def categories(request):
    return {'categories': Category.objects.all()}


def login_form(request):
    return {'login_form': UserForm()}
