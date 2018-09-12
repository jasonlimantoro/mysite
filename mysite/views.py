from django.http import HttpResponse


def home(request):
    return HttpResponse("You are logged out")