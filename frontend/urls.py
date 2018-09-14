from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='frontend.home'),
    path('categories/<int:id>', views.show_category, name='frontend.categories.show')
]

