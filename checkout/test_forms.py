from django.test import TestCase
from django.urls import reverse

from .models import Order
from .forms import OrderForm


class TestOrderForm(TestCase):
    def setUp(self):
        self.form_data = {
            'full_name': 'John Dow',
            'email': 'johndoe@example.com',
            'phone_number': '+3530123456',
            'street_address1': 'Test Street 1',
            'town_or_city': 'Test City',
            'postcode': 'A1234',
            'country': 'IE',
        }

    def test_form_valid(self):
        """
        Test if the form is valid when all required fields are provided.
        """
        form = OrderForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        """
        Test if the form is invalid when required fields are not provided.
        """
        form_data = self.form_data.copy()
        form_data['full_name'] = ''
        form_data['email'] = ''
        form_data['phone_number'] = ''
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_fields_classes(self):
        """
        Test if the form fields have the correct CSS classes.
        """
        form = OrderForm()
        for field in form.fields:
            self.assertIn(
                'stripe-style-input',
                form.fields[field].widget.attrs['class'])

    def test_form_fields_label(self):
        """
        Test if the form fields do not have labels.
        """
        form = OrderForm()
        for field in form.fields:
            self.assertFalse(form.fields[field].label)

    def test_form_fields_autofocus(self):
        """
        Test if the form fields have the autofocus attribute set correctly.
        """
        form = OrderForm()
        self.assertEqual(
            form.fields['full_name'].widget.attrs.get('autofocus'),
            True)
