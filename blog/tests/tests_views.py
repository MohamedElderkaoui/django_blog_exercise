from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from blog.models import Post, Comment
from django.contrib.auth.models import User

class UrlsTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user(username="testuser", password="12345")
        for p in range(1, 12):  # 10+1 para paginación
            Post.objects.create(
                title=f"Post {p}", slug=f"post-{p}", content="Body {}".format(p), 
                author=u, status=1
            )

    def test_home(self):
        response = self.client.get(reverse('home'))
        #self.assertEqual(response.is_paginated, True)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 3) # Está paginando a 3
        

    def test_post_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user_posts'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 10) # Está paginando a 10

        