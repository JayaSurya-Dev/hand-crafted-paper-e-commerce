from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post, Comment


class TestPostAdmin(TestCase):
    """
    Test Post Admin
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test data
        """
    # create a superuser
        cls.superuser = User.objects.create_superuser(
            username='testadmin',
            email='testadmin@email.com',
            password='testadminpassword')
        cls.superuser.save()

        # create a user
        cls.user = User.objects.create(
            username='testuser',
            email='testuser@email.com',
            password='abc123')
        cls.user.is_staff = False
        cls.user.save()

    def setUp(self):
        # create a post for testing
        self.post = Post.objects.create(
                title='test post',
                slug='test-post',
                author=self.user,
                content='test content',
                featured='False',
        )

        # create a comment for testing
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            body='test comment',
            approved='False'
        )

    def test_post_is_featured(self):
        """
        Test post is featured
        """
        # Login as an authorized staff
        login = self.client.login(
            username='testadmin',
            password='testadminpassword')
        # count how many posts are currently featured
        featured = Post.objects.filter(featured=True).count()
        self.assertTrue(self.post.featured)
        data = {
            'action': 'featured',
            '_selected_action': [self.post.id, ]
            }
        response = self.client.post(
            reverse('admin:blog_post_changelist'), data, follow=True)
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # count how many posts are currently featured
        self.assertEqual(
            Post.objects.filter(featured=True).count(), featured+1)

    def test_approved_comments(self):
        """
        Test comment is approved
        """
        # Login as an authorized staff
        login = self.client.login(
            username='testadmin',
            password='testadminpassword')
        # count how many comments are currently approved
        approved = Comment.objects.filter(approved=True).count()
        self.assertTrue(self.comment.approved)
        data = {
            'action': 'approved',
            '_selected_action': [self.comment.id, ]
            }
        response = self.client.post(
            reverse('admin:blog_comment_changelist'), data, follow=True)
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        # check number of approved comments has increased by one
        self.assertEqual(
            Comment.objects.filter(approved=True).count(), approved+1)
