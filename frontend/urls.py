from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='frontend.home'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('categories/<int:id>', views.show_category, name='frontend.categories.show')
]

