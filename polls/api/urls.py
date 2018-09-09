from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api.index'),
    path('<int:question_id>', views.show, name='api.show'),
]
