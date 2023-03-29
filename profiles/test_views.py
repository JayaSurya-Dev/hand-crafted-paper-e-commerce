from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User

from home.models import FAQ
from products.models import Product
from checkout.models import Order

from .models import UserProfile

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product


class WishListTests(TestCase):
    """
    Test wish list view
    """

    @classmethod
    def setUpTestData(cls):
        """Create test data"""

        # create an user
        cls.user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='abc123')
        cls.user.save()

    def setUp(self):
        # Login as an authorized user
        self.client.login(
            username='testuser',
            password='abc123')

        # create a product
        self.product = Product.objects.create(
                        name='test product', slug='test-product', price=10)

    def test_wishlist_url_exists_at_correct_location(self):
        """
        Test that the wish list URL exists at the correct location.
        """
        response = self.client.get("/profile/wishlist/")
        self.assertEqual(response.status_code, 200)

    def test_wishlist_url_available_by_name(self):
        """
        Test that the wish list URL is available by name.
        """
        response = self.client.get(reverse("profiles:wish_list"))
        self.assertEqual(response.status_code, 200)

    def test_wishlist_template_name_correct(self):
        """
        Test that the correct template is used to render the wish list.
        """
        response = self.client.get(reverse("profiles:wish_list"))
        self.assertTemplateUsed(response, "profiles/wishlist.html")

    def test_wishlist_template_content(self):
        """
        Test that the wish list template does not contain specific content.
        """
        response = self.client.get(reverse("profiles:wish_list"))
        self.assertNotContains(response, "Not on the page")

    def test_add_to_wishlist(self):
        """
        Test that a product can be added to the user's wishlist.
        """
        response = self.client.get(
            reverse('profiles:wish_add_remove',
                    args=[self.product.id, self.product.slug]))
        # check that the response redirects to the product detail page
        self.assertRedirects(response,
                             reverse('products:product_detail',
                                     args=[self.product.id,
                                           self.product.slug]))
        # check that the user's wishlist contains the product
        self.assertTrue(self.product.wishlist.filter(id=self.user.id).exists())

    def test_remove_from_wishlist(self):
        """
        Test that a product can be removed from the user's wishlist.
        """
        # add the product to the user's wishlist
        self.product.wishlist.add(self.user)

        # remove the product from the user's wishlist
        response = self.client.get(
                    reverse('profiles:wish_add_remove',
                            args=[self.product.id, self.product.slug]))

        # check that the response redirects to the product detail page
        self.assertRedirects(response,
                             reverse('products:product_detail',
                                     args=[self.product.id,
                                           self.product.slug]))

        # check that the user's wishlist does not contain the product
        self.assertFalse(self.product.wishlist.filter(id=self.user.id)
                         .exists())


class ProfileViewsTests(TestCase):
    """
    Test profiles app views
    """

    def setUp(self):
        """
        Set up test data
        """
        # Create a test user
        user = User.objects.create_user(
            username='testuser', password='password'
        )
        # Login as the test user
        self.client.login(username='testuser', password='password')

    def test_profile_url_exists_at_correct_location(self):
        """
        Test that the profile URL exists at the correct location
        """
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)

    def test_profile_url_available_by_name(self):
        """
        Test that the profile URL is available by name
        """
        response = self.client.get(reverse("profiles:profile"))
        self.assertEqual(response.status_code, 200)

    def test_profile_template_name_correct(self):
        """
        Test that the correct template is used to render the profile page
        """
        response = self.client.get(reverse("profiles:profile"))
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_update_profile_POST(self):
        """
        Test updating the user profile via a POST request
        """
        response = self.client.post('/profile/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(messages[0]), 'Profile updated successfully')

    def test_get_order_history(self):
        """
        Test retrieving a past order by its order number
        """
        # Create a test order
        order = Order.objects.create(
            full_name='Full Name',
            email='Email Address',
            phone_number='Phone Number',
            street_address1='Street Address 1',
            street_address2='Street Address 2',
            town_or_city='Town or City',
            county='County, State or Locality',
            postcode='Postal Code',
        )
        # Retrieve the order by its order number
        response = self.client.get(
            f'/profile/order_history/{order.order_number}'
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(messages[0]),
            f'This is a past confirmation for order '
            f'number {order.order_number}. '
            'A confirmation email was sent on the order date.'
        )
