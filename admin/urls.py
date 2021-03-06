from django.urls import path

from .views import views, category_view, blog_view, comment_view, like_view, user_view, profile_view

app_name = 'admin'
urlpatterns = [
    path('', views.index, name='index'),
    # categories
    path('categories', category_view.index, name='categories.index'),
    path('categories/create', category_view.create, name='categories.create'),
    path('categories/store', category_view.store, name='categories.store'),
    path('categories/<int:category_id>', category_view.update, name='categories.update'),
    path('categories/<int:category_id>/delete', category_view.destroy, name='categories.destroy'),
    path('categories/<int:category_id>/show', category_view.show, name='categories.show'),
    path('categories/<int:category_id>/edit', category_view.edit, name='categories.edit'),

    # blogs
    path('blogs', blog_view.index, name='blogs.index'),
    path('blogs/create', blog_view.create, name='blogs.create'),
    path('blogs/store', blog_view.store, name='blogs.store'),
    path('blogs/<int:blog_id>/delete', blog_view.destroy, name='blogs.destroy'),
    path('blog/<int:blog_id>/edit', blog_view.edit, name='blogs.edit'),
    path('blog/<int:blog_id>', blog_view.update, name='blogs.update'),
    path('blog/<int:blog_id>/show', blog_view.show, name='blogs.show'),

    # comments
    path('blog/<int:blog_id>/comments', comment_view.store, name='comments.store'),
    path('blog/<int:blog_id>/comments/<int:comment_id>/edit', comment_view.edit, name='comments.edit'),
    path('comments/<int:comment_id>', comment_view.update, name='comments.update'),
    path('comments/<int:comment_id>/delete', comment_view.destroy, name='comments.destroy'),
    path('comments/<int:comment_id>/toggle_visibility', comment_view.toggle_visibility, name='comments.toggle_visibility'),

    # like
    path('blog/<int:blog_id>/like/store', like_view.store, name='like.store'),
    path('blog/<int:blog_id>/like/delete', like_view.destroy, name='like.destroy'),

    # users
    path('users', user_view.index, name='users.index'),
    path('user/<int:user_id>/ban', user_view.toggle_ban, name='users.toggle_ban'),
    path('user/<int:user_id>/show', user_view.show, name='users.show'),
    path('users/create', user_view.create, name='users.create'),
    path('users/store', user_view.store, name='users.store'),

    # profile
    path('profile/<int:profile_id>', profile_view.update, name='profiles.update')
]

