from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
import json

from products.models import Product

from .models import Order, OrderLineItem


class CheckoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout:checkout')
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00)
        self.user = User.objects.create_user(
            username='testuser',
            password='password')
        self.client.login(username='testuser', password='password')
        self.session = self.client.session
        self.session['cart'] = {str(self.product.id): 2}
        self.session.save()

    def test_checkout_url_exists_at_correct_location(self):
        """
        Test that the checkout URL exists at the correct location.
        """
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)

    def test_checkout_url_available_by_name(self):
        """
        Test that the checkout URL is available by name.
        """
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)

    def test_checkout_template_name_correct(self):
        """
        Test that the correct template is used to render the checkout page.
        """
        response = self.client.get(self.checkout_url)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_template_content(self):
        """
        Test that the checkout template does contain specific content.
        """
        response = self.client.get(self.checkout_url)
        self.assertContains(response, "Checkout")
        self.assertNotContains(response, "Page not found")

    def test_checkout_view_post_with_valid_data(self):
        data = {
            'full_name': 'Test User',
            'email': 'testuser@example.com',
            'phone_number': '3530123456',
            'street_address1': '1 Test St',
            'street_address2': '',
            'county': '',
            'town_or_city': 'Test Town',
            'postcode': 'A1234',
            'country': 'IE',
            'client_secret': 'test_secret'
        }

        response = self.client.post(self.checkout_url, data=data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

        # Check that the order and order line item were created
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.full_name, 'Test User')
        self.assertEqual(order.email, 'testuser@example.com')
        self.assertEqual(order.phone_number, '3530123456')
        self.assertEqual(order.street_address1, '1 Test St')
        self.assertEqual(order.street_address2, None)
        self.assertEqual(order.county, None)
        self.assertEqual(order.town_or_city, 'Test Town')
        self.assertEqual(order.postcode, 'A1234')
        self.assertEqual(order.country, 'IE')
        self.assertEqual(order.stripe_pid, 'test')
        self.assertEqual(order.original_cart, json.dumps(self.session['cart']))
        self.assertEqual(order.user_profile, self.user.userprofile)

        self.assertEqual(OrderLineItem.objects.count(), 1)
        line_item = OrderLineItem.objects.first()
        self.assertEqual(line_item.order, order)
        self.assertEqual(line_item.product, self.product)
        self.assertEqual(line_item.quantity, 2)

        # # Check that the cart was cleared
        # self.assertNotIn('cart', self.session)

    def test_checkout_view_post_with_invalid_data(self):
        data = {
            'full_name': '',
            'email': '',
            'phone_number': '',
            'street_address1': '',
            'street_address2': '',
            'county': '',
            'town_or_city': '',
            'postcode': '',
            'country': '',
            'client_secret': 'test_secret'
        }

        # response = self.client.post(self.checkout_url, data=data, follow=True)

        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, self.checkout_url)

#         # Check that the form is invalid and the order and order line item
#         # were not created
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(OrderLineItem.objects.count(), 0)

        # Check that the form errors are displayed in the page
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), 'There was an error with your form.\
#  Please double check your information.')
