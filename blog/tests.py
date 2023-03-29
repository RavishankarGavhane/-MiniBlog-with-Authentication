from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Home, Contact, Category, Post, Comment

class HomeModelTest(TestCase):

    def setUp(self):
        Home.objects.create(title="Test Home Title",
                            about="Test Home About",
                            copyright="Test Home Copyright",
                            address="Test Home Address",
                            phone="Test Home Phone",
                            email="Test Home Email")

    def test_home_str(self):
        home = Home.objects.get(title="Test Home Title")
        self.assertEqual(str(home), "Test Home Title")


class ContactModelTest(TestCase):

    def setUp(self):
        Contact.objects.create(first_name="Test First Name",
                               last_name="Test Last Name",
                               email="Test Email",
                               subject="Test Subject",
                               message="Test Message")

    def test_contact_str(self):
        contact = Contact.objects.get(first_name="Test First Name")
        self.assertEqual(str(contact), "Test First Name")


class CategoryModelTest(TestCase):

    def setUp(self):
        Category.objects.create(title="Test Category Title")

    def test_category_str(self):
        category = Category.objects.get(title="Test Category Title")
        self.assertEqual(str(category), "Test Category Title")


class PostModelTest(TestCase):

    def setUp(self):
        category = Category.objects.create(title="Test Category Title")
        Post.objects.create(title="Test Post Title",
                            category=category,
                            text="Test Post Text")

    def test_post_str(self):
        post = Post.objects.get(title="Test Post Title")
        self.assertEqual(str(post), "Test Post Title")

    def test_post_slug(self):
        post = Post.objects.get(title="Test Post Title")
        self.assertEqual(post.slug, "test-post-title")


class CommentModelTest(TestCase):

    def setUp(self):
        category = Category.objects.create(title="Test Category Title")
        post = Post.objects.create(title="Test Post Title",
                                   category=category,
                                   text="Test Post Text")
        Comment.objects.create(name="Test Comment Name",
                               email="Test Comment Email",
                               post=post,
                               message="Test Comment Message")

    def test_comment_str(self):
        comment = Comment.objects.get(name="Test Comment Name")
        self.assertEqual(str(comment), "Test Comment Name")
