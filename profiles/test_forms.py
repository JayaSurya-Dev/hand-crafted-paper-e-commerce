from django.test import TestCase

from profiles.forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """
    Test for the profiles app forms
    """

    def test_user_profile_form(self):
        """
        Testing the user profile form
        """
        form = UserProfileForm(data={
            'default_full_name': 'Test User',
            'default_email': 'testuser@email.com',
            'default_phone_number': '03530123456',
            'default_street_address1': '123 Main St',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Anytown',
            'default_county': 'Anycounty',
            'default_postcode': 'A1234',
            'default_country': 'IE',
        })

        self.assertTrue(form.is_valid())
