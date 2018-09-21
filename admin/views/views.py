from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from frontend.models import Category


@login_required
def index(request):
    categories = Category.objects.all()
    user = request.user
    return render(request, 'admin/index.html', {
        'categories': categories,
        'user': user,
    })

