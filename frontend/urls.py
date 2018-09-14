from . import views
from django.urls import path

app_name = 'frontend'
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('categories/<int:id>', views.show_category, name='categories.show'),

    # blog
    path('blog/<int:id>', views.show_blog, name='blogs.show')
]

