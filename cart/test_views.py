from django.test import TestCase, Client
from decimal import Decimal
from django.urls import reverse
from django.contrib.messages import get_messages

from products.models import Product


class CartViewTests(TestCase):
    """
    Module containing tests for the cart view of the web application.
    """
    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.url = reverse('cart:view_cart')

    def test_cart_view_url_exists_at_correct_location(self):
        """
        The cart view URL is accessible and returns a 200 status code.
        """
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)

    def test_cart_view_url_available_by_name(self):
        """
        The cart view URL can be accessed using its name `cart:view_cart`.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_cart_view_template_name_correct(self):
        """
        The correct template `cart/cart.html` is used to render the cart view.
        """
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "cart/cart.html")

    def test_cart_view_template_content(self):
        """
        The rendered template contains the text "Shopping Cart" and does
        not contain the text "Page not found".
        """
        response = self.client.get(self.url)
        self.assertContains(response, "Shopping Cart")
        self.assertNotContains(response, "Page not found")


class AddToCartViewTests(TestCase):
    """
    Test add to cart view
    """
    def setUp(self):
        """
        Create test data
        """
        self.client = Client()
        # create a product for testing
        self.product = Product.objects.create(
            name='test product',
            slug='test-product',
            description='test cake topper description',
            price=Decimal('10.00'),
            available=True)

        self.url = reverse('cart:view_cart')

    def test_add_to_cart_template_content(self):
        """
        Test that the shopping cart view contains expected content
        """
        response = self.client.get(self.url)
        self.assertContains(response, "Shopping Cart")
        self.assertNotContains(response, "Page not found")

    def test_add_to_cart_item_quantity_with_invalid_input(self):
        """
        Test adding a product to cart with invalid quantity input
        """
        add_url = reverse('cart:add_to_cart', args=[self.product.id])
        adjust_url = reverse('cart:adjust_cart', args=[self.product.id])
        response = self.client.post(add_url,
                                    {'quantity': '',
                                     'redirect_url': self.url},)
        # Verify that the response redirects to the cart page
        self.assertEqual(response.status_code, 302)
        response = self.client.post(adjust_url,
                                    {'quantity': '1',
                                     'redirect_url': self.url},)
        # Verify that the response redirects to the cart page
        self.assertEqual(response.status_code, 302)

        # Verify that an error message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Quantity must be a digit.'
        )

    def test_add_to_cart_item_with_no_size_POST(self):
        """
        Test adding a product to cart with no size specified
        """
        url = reverse('cart:add_to_cart', args=[self.product.id])
        data = {'quantity': 1,
                'redirect_url': self.url,
                }
        response = self.client.post(url, data=data)

        # Verify that the product is added to the cart
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 1)

        # Verify that a success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Added {self.product.name} to your cart'
        )

    def test_add_to_cart_item_with_size_POST(self):
        """
        Test adding a product to cart with a size specified
        """
        url = reverse('cart:add_to_cart', args=[self.product.id])
        data = {'quantity': 1,
                'redirect_url': self.url,
                'product_size': '9x9in',
                }
        response = self.client.post(url, data=data)

        # Verify that the product is added to the cart with the correct size
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)],
                         {'items_by_size': {'9x9in': 1}})

        # Verify that a success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            f'Added size 9X9IN {self.product.name} to your cart'
        )

    def test_add_to_cart_same_item_with_no_size_twice(self):
        """
        Test adding same product with no size to the cart twice
        """
        add_url = reverse('cart:add_to_cart', args=[self.product.id])

        # add the product to the cart once
        self.client.post(
            add_url,
            {'quantity': 1, 'redirect_url': self.url})
        # add the product to the cart again
        response = self.client.post(add_url,
                                    {'quantity': 1, 'redirect_url': self.url})
        cart = self.client.session['cart']

        # check that the quantity of the product in the cart is 2
        self.assertEqual(cart[str(self.product.id)], 2)

        # assert toast message is correct
        messages = list(get_messages(response.wsgi_request))
        # check that the success message indicates the quantity has been
        # updated
        self.assertEqual(
            str(messages[1]),
            f'Updated {self.product.name} quantity to \
{cart[str(self.product.id)]}')

    def test_add_to_cart_same_item_with_size_twice(self):
        # Test adding the same product with no size to the cart twice
        add_url = reverse('cart:add_to_cart', args=[self.product.id])

        # add the product with size to the cart once
        self.client.post(
            add_url,
            {'quantity': 1,
             'redirect_url': self.url,
             'product_size': '9x9in',
             })
        # add the product with size to the cart again
        response = self.client.post(
            add_url,
            {'quantity': 1,
             'redirect_url': self.url,
             'product_size': '9x9in',
             })
        cart = self.client.session['cart']

        # check that the quantity of the product in the cart with the 
        # specified size is 2
        self.assertEqual(cart[str(self.product.id)],
                         {'items_by_size': {'9x9in': 2}})

        # assert toast message is correct
        messages = list(get_messages(response.wsgi_request))
        # check that the success message indicates the quantity has been
        # updated
        self.assertEqual(
            str(messages[1]),
            f'Updated size 9X9IN {self.product.name} quantity \
to 2')


class UpdateCartViewTests(TestCase):
    """
    Test update cart view
    """
    def setUp(self):
        """
        Create test data
        """
        self.client = Client()
        # create a product for testing
        self.product = Product.objects.create(
            name='test product',
            slug='test-product',
            description='test cake topper description',
            price=Decimal('10.00'),
            available=True)

        self.url = reverse('cart:view_cart')

    def test_adjust_cart_quantity_with_invalid_input(self):
        """
        Test adjusting cart quantity with invalid input
        """
        add_url = reverse('cart:add_to_cart', args=[self.product.id])
        adjust_url = reverse('cart:adjust_cart', args=[self.product.id])

        # Test adjusting cart quantity with an empty input
        response = self.client.post(adjust_url,
                                    {'quantity': '',
                                     'redirect_url': self.url},)
        self.assertEqual(response.status_code, 302)

        # Test adjusting cart quantity with a valid input
        response = self.client.post(adjust_url,
                                    {'quantity': '1',
                                     'redirect_url': self.url},)
        self.assertEqual(response.status_code, 302)

        # assert toast message is correct
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Quantity must be a digit.'
        )

    def test_adjust_cart_quantity_POST(self):
        """
        Test adjusting cart quantity via POST request
        """
        cart = {'1': 1}
        self.client.session['cart'] = cart
        self.client.session.save()

        # POST request to adjust quantity to 2
        adjust_url = reverse('cart:adjust_cart', args=[self.product.id])
        data = {'quantity': 2}
        response = self.client.post(adjust_url, data=data)

        # Check that the cart is updated with new quantity
        expected_cart = {'1': 2}
        self.assertEqual(self.client.session['cart'], expected_cart)

        self.assertRedirects(response, self.url)

    def test_adjust_cart_item_with_no_size(self):
        """
        Test adjusting cart item with no size
        """
        add_url = reverse('cart:add_to_cart', args=[self.product.id])
        adjust_url = reverse('cart:adjust_cart', args=[self.product.id])

        # Add product to cart
        response = self.client.post(add_url,
                                    {'quantity': 1,
                                     'redirect_url': self.url},)
        self.assertEqual(response.status_code, 302)

        # Test adjusting cart item quantity
        response = self.client.post(adjust_url,
                                    {'quantity': 2,
                                     'redirect_url': self.url},)
        self.assertEqual(response.status_code, 302)

        # Test removing cart item from cart
        response = self.client.post(adjust_url,
                                    {'quantity': 0,
                                     'redirect_url': self.url},)
        self.assertEqual(response.status_code, 302)

        # assert toast message is correct
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]),
                         f'Updated {self.product.name} quantity to 2')
        self.assertEqual(str(messages[2]),
                         f'Removed {self.product.name} from your cart')
        self.assertRedirects(response, self.url)

    def test_adjust_cart_item_with_size(self):
        """
        Test adjusting cart item with size
        """
        add_url = reverse('cart:add_to_cart', args=[self.product.id])
        adjust_url = reverse('cart:adjust_cart', args=[self.product.id])

        # Add product to cart with size
        self.client.post(
            add_url,
            {'quantity': 1, 'redirect_url': self.url,
             'product_size': '9x9in'},)

        # Test adjusting cart item quantity adding 1
        self.client.post(
            adjust_url,
            {'quantity': 2, 'redirect_url': self.url,
             'product_size': '9x9in'},)

        # Test adjusting cart item quantity to 0
        response = self.client.post(
            adjust_url,
            {'quantity': 0, 'redirect_url': self.url,
             'product_size': '9x9in'},)

        # assert toast message is correct
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Updated size 9X9IN {self.product.name} quantity to 2'
        )
        self.assertEqual(
            str(messages[2]),
            f'Removed size 9X9IN {self.product.name} from your cart'
        )
        self.assertRedirects(response, self.url)


class RemoveFromCartViewTest(TestCase):
    """
    Test remove from cart view
    """
    def setUp(self):
        """
        Create test data for each test method
        """
        self.client = Client()
        # create a product for testing
        self.product = Product.objects.create(
            name='test product',
            slug='test-product',
            description='test cake topper description',
            price=Decimal('10.00'),
            available=True)

        self.cart_url = reverse('cart:view_cart')

    def test_remove_from_cart_item_with_no_size(self):
        """
        Test that a user can remove a product without size from their cart.
        Test that the toast message displayed is correct.
        """
        add_url = reverse('cart:add_to_cart', args=[self.product.id])
        remove_url = reverse('cart:remove_from_cart', args=[self.product.id])

        # add product to cart
        self.client.post(
            add_url,
            {'quantity': 1, 'redirect_url': self.cart_url},)
        # remove product from cart
        response = self.client.post(remove_url)

        # assert toast message is correct
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Removed {self.product.name} from your cart'
        )

    def test_remove_from_cart_item_with_size(self):
        """
        Test that a user can remove a product with size from their cart.
        Test that the toast message displayed is correct.
        """
        add_url = reverse('cart:add_to_cart', args=[self.product.id])
        remove_url = reverse('cart:remove_from_cart', args=[self.product.id])

        # add product with size to cart
        self.client.post(
            add_url,
            {'quantity': 1, 'redirect_url': self.cart_url,
             'product_size': '9x9in'},)
        # remove product with size from cart
        self.client.post(
            remove_url,
            {'quantity': 1, 'redirect_url': self.cart_url,
             'product_size': '9x9in'},)
        # assert cart is empty after removing product with size
        response = self.client.post(remove_url)
        cart = self.client.session['cart']
        self.assertEqual(cart, {})
        # assert toast message is correct
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            f'Removed size 9X9IN {self.product.name} from your cart'
        )
