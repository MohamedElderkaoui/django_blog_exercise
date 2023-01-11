from datetime import timedelta, timezone
import tabnanny
from django.test import TestCase
from ..models import User, Post, Comment
from django.contrib.auth.models import User
# Create your tests here.
'''
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

'''
from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from ..models import Post, Comment

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Luis', last_name='Bob')
        p = Post.objects.create(title='My first post', 
            slug='my-first-post', 
            author=u,
            content='My first post content')
        Comment.objects.create(
            post=p, 
            name='MarÃ­a',
            email = 'maria@gmail.com',
            body = 'My first comment'
            )

    def test_metodo_str(self):
        '''
        Comprobar que el print del objeto devuelve su tÃ­tulo
        '''
        post = Post.objects.first()
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, str(post))

    def test_slug(self):
        '''
        Comprobar el slug
        '''
        post = Post.objects.first()
        slug = post.slug
        expected_slug = post.title.lower().replace(' ', '-')
        self.assertEquals(expected_slug, slug)
        
    def test_str_comentario(self):
        c = Comment.objects.first()
        expected_object_name = f'Comment {c.body} by {c.name}'
        self.assertEquals(expected_object_name, str(c))

from django.test import TestCase
from ..models import Comment, Post

class CommentModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post")
        self.comment = Comment.objects.create(
            post=self.post,
            name="Test User",
            email="testuser@example.com",
            body="This is a test comment"
        )

    def test_comment_str(self):
        self.assertEqual(str(self.comment), "Comment This is a test comment by Test User")

    def test_comment_ordering(self):
        comment2 = Comment.objects.create(
            post=self.post,
            name="Another Test User",
            email="anothertestuser@example.com",
            body="This is another test comment",
            created_on=self.comment.created_on + timedelta(seconds=1)
        )
        self.assertEqual(list(Comment.objects.all()), [self.comment, comment2])
class CommentActiveTest(TestCase):
    def test_comment_active_default(self):
        post = Post.objects.create(title="Test post")
        comment = Comment.objects.create(post=post, name="Test User", email="testuser@example.com", body="Test comment")
        self.assertFalse(comment.active)
    
    def test_comment_active_set_True(self):
        post = Post.objects.create(title="Test post")
        comment = Comment.objects.create(post=post, name="Test User", email="testuser@example.com", body="Test comment", active=True)
        self.assertTrue(comment.active)

    def test_comment_active_set_False(self):
        post = Post.objects.create(title="Test post")
        comment = Comment.objects.create(post=post, name="Test User", email="testuser@example.com", body="Test comment", active=False)
        self.assertFalse(comment.active)
class CommentActiveTest(TestCase):
    def test_comment_active_default(self):
        post = Post.objects.create(title="Test post")
        comment = Comment.objects.create(post=post, name="Test User", email="testuser@example.com", body="Test comment")
        self.assertFalse(comment.active)
    
    def test_comment_active_set_True(self):
        post = Post.objects.create(title="Test post")
        comment = Comment.objects.create(post=post, name="Test User", email="testuser@example.com", body="Test comment", active=True)
        self.assertTrue(comment.active)

    def test_comment_active_set_False(self):
        post = Post.objects.create(title="Test post")
        comment = Comment.objects.create(post=post, name="Test User", email="testuser@example.com", body="Test comment", active=False)
        self.assertFalse(comment.active)