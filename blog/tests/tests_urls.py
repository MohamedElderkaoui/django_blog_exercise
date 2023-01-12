from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from blog.models import Post, Comment
from django.contrib.auth.models import User

class UrlsTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user(username="testuser", password="12345")
        for p in range(1, 11):
            Post.objects.create(
                title=f"Post {p}", slug=f"post-{p}", content="Body {}".format(p), author=u
            )

    def test_urls(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('post_detail', kwargs={'slug': 'post-1'}))
        self.assertEqual(response.status_code, 200)
        
    def test_user_posts_nologin(self):
        response = self.client.get(reverse('user_posts'))
        self.assertRedirects(response, '/accounts/login/?next=/mis-posts/') # No está logueado. Redirige a login
    
    def test_user_posts_login(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user_posts'))
        self.assertEqual(response.status_code, 200)


        