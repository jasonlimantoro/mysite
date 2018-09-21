from faker import Faker
from django.test import TestCase
from django.contrib.auth.models import User

from polls.models import Blog, Like

faker = Faker()


class UserLikesBlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=faker.first_name_female(), email=faker.free_email(),
                                        password=faker.word())
        self.blog = self.user.blogs.create(title=faker.sentence(nb_words=3), description=faker.paragraph())

    def test_blog_and_user_should_have_one_like(self):
        """
        oh ternyata ada test disini lol
        tapi untuk test ini kurang bermakna sih. soalnya ini kan kayak ngetest db driver sama relationship modelnya
        biasanya yg di test itu: manager (unit test) atau view (integration test)
        kayak contoh bikin like_manager.py
        trus didalamnya ada function:
        """
        def like_blog(blog: Blog, operator: User):
            """
            add Like to {blog} by {operator}
            """
            Like.objects.create(blog_id=blog.id, user_id=operator.id)
        """
        nah kalo ada function kayak diatas, di test ini bisa di test
        
        like_manager.like_blog(blog=self.blog, operator=self.user)
        self.assertEqual(self.user.like_set.count(), 1)
        self.assertEqual(self.blog.like_set.count(), 1)
        
        kalo gini kan ibaratnya ngetest managernya, jadi dari test ini ngasih tau kalo misalnya mau like, panggil function
        like_manager.like_blog itu harusnya bakal ke like postnya dengan benar
        
        tapi buat ngecek apakah view bener2 manggil function ini pas tombol like di klik, itu mesti simulate requestnya
        https://docs.djangoproject.com/en/1.11/topics/testing/tools/
        """


        self.user.like_set.create(blog=self.blog)
        self.assertEqual(self.user.like_set.count(), 1)
        self.assertEqual(self.blog.like_set.count(), 1)
