from django.test import TestCase, Client
from home.forms import ContactForm


class TestContactForm(TestCase):
    """Test contact form"""

    def test_contact_form_with_valid_data(self):
        """test contact form with valid data"""
        form = ContactForm(data={
            'name': 'testuser',
            'email': 'testuser@email.com',
            'content': 'some contact form content'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_with_no_data(self):
        """test contact form with no data"""
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
