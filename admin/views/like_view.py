from polls.models import Like, Blog
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.shortcuts import reverse


@require_http_methods(['POST'])
def store(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    Like.objects.create(user=request.user, blog=blog)
    messages.success(request, "Successfully liked this post!")
    return HttpResponseRedirect(reverse('admin:blogs.show', args=(blog_id,)))


@require_http_methods(['POST'])
def destroy(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.like_set.filter(user=request.user).delete()
    messages.success(request, "Successfully unliked this post!")
    return HttpResponseRedirect(reverse('admin:blogs.show', args=(blog_id,)))

