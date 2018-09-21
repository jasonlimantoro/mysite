from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='blogs')
    likes = models.ManyToManyField(User, through='Like', through_fields=('blog', 'user'), related_name='blog')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='blogs')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liked_at = models.DateTimeField('liked at', default=timezone.now)


class Profile(models.Model):
    DEFAULT_IMAGE_URL = 'default.png'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True, default=DEFAULT_IMAGE_URL)

    def has_default_image(self):
        return self.image == self.DEFAULT_IMAGE_URL

    def set_image_to_default(self):
        if not self.has_default_image():
            self.image.delete()
            self.image = self.DEFAULT_IMAGE_URL
            self.save()
        return self
