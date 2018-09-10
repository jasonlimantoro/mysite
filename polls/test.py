import datetime

from faker import Faker
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Question, Blog, Like

faker = Faker()

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
class UserLikesBlogTests(TestCase):
    def test_blog_should_have_one_like(self):
        user = User.objects.create_user(username=faker.first_name_female(), email=faker.free_email(), password=faker.word())
        blog = Blog.objects.create(title=faker.sentence(), description=faker.paragraph(), user=user)
        Like.objects.create(user=user, blog=blog)
        self.assertEqual(user.like_set.count(), 1)
        self.assertEqual(blog.like_set.count(), 1)