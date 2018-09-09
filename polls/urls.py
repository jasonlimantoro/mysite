from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.ShowView.as_view(), name='show'),
    path('<int:pk>/edit', views.EditView.as_view(), name='edit'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
