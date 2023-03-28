from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from blog.models import Post, Comment


class PostModelTest(TestCase):
    """
    Test Post Model
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', password='password')

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user,
            content='This is a test post content.',
            status=Post.Status.PUBLISHED,
            published=timezone.now())

    def test_create_post(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.content, 'This is a test post content.')
        self.assertEqual(self.post.status, Post.Status.PUBLISHED)

    def test_post_slug(self):
        self.assertEqual(self.post.slug, 'test-post')

    def test_post_absolute_url(self):
        url = self.post.get_absolute_url()
        self.assertEqual(url, f'/blog/article/{self.post.slug}/')


class CommentModelTest(TestCase):
    """
    Test Comment Model
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', password='password')
        cls.post = Post.objects.create(
            title='Test Post',
            author=cls.user,
            content='This is a test post content.',
            status=Post.Status.PUBLISHED,
            published=timezone.now())

    def setUp(self):
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            email='testuser@email.com',
            body='This is a test comment body.')

    def test_create_comment(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.email, 'testuser@email.com')
        self.assertEqual(self.comment.body, 'This is a test comment body.')
        self.assertFalse(self.comment.approved)

    def test_approve_comment(self):
        self.comment.approved = True
        self.comment.save()
        self.assertTrue(self.comment.approved)

    def test_comment_model_str_representation(self):
        """Test Comment model return string representation"""
        data = self.comment
        self.assertEqual(
            data.__str__(), 'testuser')
