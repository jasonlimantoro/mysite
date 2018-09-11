from django.urls import path

from . import views
from .categories import views as category_view

app_name = 'admin'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories', category_view.index, name='categories.index'),
    path('categories/<int:category_id>/show', category_view.show, name='categories.show'),
    path('categories/<int:category_id>', category_view.edit, name='categories.edit')
]
