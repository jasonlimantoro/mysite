from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker

# Create your tests here.
faker = Faker()


class UserLikesBlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=faker.first_name_female(), email=faker.free_email(),
                                        password=faker.word())
        self.blog = self.user.blogs.create(title=faker.sentence(nb_words=3), description=faker.paragraph())

    def test_blog_and_user_should_have_one_like(self):
        self.user.like_set.create(blog=self.blog)
        self.assertEqual(self.user.like_set.count(), 1)
        self.assertEqual(self.blog.like_set.count(), 1)
