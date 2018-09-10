import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='blogs')
    likes = models.ManyToManyField(User, through='Like', through_fields=('blog', 'user'), related_name='blog')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='blogs')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):

    def __str__(self):
        return self.content
    
    content = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('date published', default=timezone.now)

class Like(models.Model):
    class Meta:
        unique_together=("user", "blog")

    def __str__(self):
        return "'%s' likes '%s'" % (self.user.username, self.blog.title)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liked_at = models.DateTimeField('liked at', default=timezone.now)
