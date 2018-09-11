from django.urls import path

from .views import views, category_view, blog_view

app_name = 'admin'
urlpatterns = [
    path('', views.index, name='index'),
    # categories
    path('categories', category_view.index, name='categories.index'),
    path('categories/<int:category_id>/show', category_view.show, name='categories.show'),
    path('categories/<int:category_id>/edit', category_view.edit, name='categories.edit'),
    path('blogs', blog_view.index, name='blogs.index'),
    path('blog/<int:blog_id>/edit', blog_view.edit, name='blogs.edit'),
    path('blog/<int:blog_id>', blog_view.update, name='blogs.update')
]
