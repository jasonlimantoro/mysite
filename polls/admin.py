from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Question, Choice
from frontend.models import Category, Blog, Comment, Like

# Unregister unecessary models
admin.site.unregister(Group)

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content', {'fields': ['title', 'description']}),
        ('Category', {'fields': ['category']})
    ]
    list_display = ('title', 'description', 'categorized_to', 'pub_date')
    search_fields = ['title', 'description']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class CommentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    
    list_display = ('content', 'blog_id', 'pub_date')
    search_fields = ['content']

class LikeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    
    list_display = ('user_id', 'blog_id')

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)


