from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from profiles.models import UserProfile

UserProfile = User


class TestUserProfileModel(TestCase):
    """
    Test UserProfile model
    """
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@email.com',
            password='abc123',
            )

    def test_user_profile_model_name_str_(self):
        """Test UserProfile model return name"""
        data = self.user.username
        self.assertEqual(
            data.__str__(), 'testuser')
