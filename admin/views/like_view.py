from polls.models import Like, Blog
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.shortcuts import reverse


@require_http_methods(['POST'])
def store(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    request.user.like_set.create(blog=blog)
    # Like.objects.create(user=request.user, blog=blog)
    # kenapa gk pake yg ini aja? lebih rapi gk banyak chainnya ^^
    # dan klo mau hemat db query, bisa gni
    # Like.objects.create(user_id=request.user.id, blog_id=blog.id)
    messages.success(request, "Successfully liked this post!")
    return HttpResponseRedirect(reverse('admin:blogs.show', args=(blog_id,)))


@require_http_methods(['POST'])
def destroy(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    # kalo udah cascade hrsnay gk apa sih
    blog.like_set.filter(user=request.user).delete()
    messages.success(request, "Successfully unliked this post!")
    return HttpResponseRedirect(reverse('admin:blogs.show', args=(blog_id,)))

