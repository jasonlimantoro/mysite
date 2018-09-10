from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Question, Choice, Blog, Category

# Unregister unecessary models
admin.site.unregister(Group)

class BlogAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

admin.site.site_header = "My coolest blog"
admin.site.index_title = "Models"

