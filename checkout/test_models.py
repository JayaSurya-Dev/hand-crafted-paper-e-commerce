from decimal import Decimal

from django.test import TestCase
from django.conf import settings

from django.contrib.auth.models import User

from products.models import Product
from profiles.models import UserProfile

from .models import Order, OrderLineItem


class TestOrderLineItemModel(TestCase):
    """
    Test the OrderLineItem model
    """

    def setUp(self):
        """
        Set up test data for OrderLineItem model
        """
        # Create a test user and user profile
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )
        self.user_profile, created = UserProfile.objects.update_or_create(
            user=self.user,
            defaults={
                'default_phone_number': '003530123456',
                'default_street_address1': '1 Main St',
                'default_town_or_city': 'Test Town',
                'default_postcode': 'A1234',
                'default_country': 'IE',
            }
        )
        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            price=Decimal('9.99'),
            sku='ABC123'
        )
        # Create a test order
        self.order = Order.objects.create(
            full_name='Test User',
            email='testuser@example.com',
            phone_number='003530123456',
            country='IE',
            postcode='A1234',
            town_or_city='Test Town',
            street_address1='1 Main St',
            street_address2='',
            county='',
            delivery_cost=0,
            order_total=Decimal('9.99'),
            grand_total=Decimal('9.99'),
            original_cart='',
            stripe_pid=''
        )
        # Create a test order line item
        self.order_line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            product_size=None,
            quantity=1,
            lineitem_total=Decimal('9.99')
        )

    def test_order_str_method(self):
        """
        Test that the __str__ method of Order returns
        the expected string
        """
        # Get the expected result
        expected_result = f'{self.order.order_number}'
        self.assertEqual(str(self.order), expected_result)

    def test_order_line_item_str_method(self):
        """
        Test that the __str__ method of OrderLineItem returns
        the expected string
        """
        # Get the expected result
        expected_result = f'SKU {self.product.sku} on order \
{self.order.order_number}'
        self.assertEqual(str(self.order_line_item), expected_result)

    def test_order_line_item_save_method(self):
        """
        Test that the save method of OrderLineItem updates the
        lineitem_total and order_total as expected
        """
        # Increase the quantity of the order line item
        self.order_line_item.quantity = 2
        self.order_line_item.save()
        # Get the expected line item total
        expected_lineitem_total = self.product.price * 2
        # Check that the line item total is equal to the expected
        # line item total
        self.assertEqual(
            self.order_line_item.lineitem_total, expected_lineitem_total)

        # Get the expected order total
        expected_order_total = Decimal('19.98')
        # Check that the order total is equal to the expected order total
        self.assertEqual(self.order.order_total, expected_order_total)

        # Get the expected delivery cost
        expected_delivery_cost = expected_order_total * \
            settings.STANDARD_DELIVERY_PERCENTAGE / 100
        # Get the expected grand total
        expected_grand_total = expected_order_total + expected_delivery_cost
        self.assertEqual(self.order.grand_total, expected_grand_total)
