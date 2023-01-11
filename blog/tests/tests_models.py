from django.test import TestCase

# Create your tests here.
from blog.models import Post, Comment
from django.contrib.auth.models import User

class PostTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user(username="testuser", password="12345")
        for p in range(1, 11):
            Post.objects.create(
                title=f"Post {p}", slug=f"post-{p}", content="Body {}".format(p), author=u
            )

    def test_slug(self):
        post = Post.objects.get(title="Post 1")
        self.assertEqual(post.slug, "post-1")
    
    def test_str(self):
        post = Post.objects.get(title="Post 1")
        self.assertEqual(str(post), "Post 1")
