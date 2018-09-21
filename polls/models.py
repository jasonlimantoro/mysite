import os
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
# klo gk dipake dihapus aja nih
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# klo gk dipake dihapus aja nih
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)  # bisa kalo pake TextField gk perlu kasih max_length
    # semua yg pub_date begini, bisa dikasih auto_now_add aja, daripada default, coba dibaca docsnya tentang auto_now_add
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

class Blog(models.Model):  # ini mungkin lebih cocok dinamain Post, tapi gk apa2
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='blogs')
    likes = models.ManyToManyField(User, through='Like', through_fields=('blog', 'user'), related_name='blog')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='blogs')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

    def categorized_to(self):  # ini gk dipake ya
        return self.category.title

    def is_liked_by(self, user):
        return self.like_set.filter(user_id=user.id).exists()


class Comment(models.Model):

    def __str__(self):
        return self.content

    content = models.TextField(max_length=200)
    is_hidden = models.BooleanField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('date published', default=timezone.now)


class Like(models.Model):
    class Meta:
        unique_together = ("user", "blog")

    def __str__(self):  # ini gk bagus kalo dijadiin default __str__, mending bikin function kyk .as_text() gitu, soalnya kalo ngk, ini bkl dipanggil terus dimana2
        return "'%s' likes '%s'" % (self.user.username, self.blog.title)

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liked_at = models.DateTimeField('liked at', default=timezone.now)


class Profile(models.Model):
    default_image_url = 'default.png'  # kalo constant di uppercase aja
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True, default=default_image_url)

    def has_default_image(self):
        return self.image == self.default_image_url

    def set_image_to_default(self):
        if not self.has_default_image():
            self.image.delete()
            self.image = self.default_image_url
            self.save()
        return self
