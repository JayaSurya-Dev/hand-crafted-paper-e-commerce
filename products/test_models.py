from decimal import Decimal
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Product, ProductReview


class CategoryModelTest(TestCase):
    """
    Test Category Model
    """
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name='TestCategory',
            slug='test-category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_friendly_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_friendly_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.name
        self.assertEqual(str(category), expected_object_name)

    def test_get_friendly_name_returns_friendly_name(self):
        category = Category.objects.get(id=1)
        friendly_name = 'Test Friendly Name'
        category.friendly_name = friendly_name
        category.save()
        self.assertEqual(category.get_friendly_name(), friendly_name)


class ProductModelTest(TestCase):
    """
    Test Product Model
    """
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            name='TestCategory',
            slug='test-category')
        Product.objects.create(
            category=category,
            sku='testsku',
            name='TestProduct',
            slug='test-product',
            description='Test Description',
            price=Decimal('10.00'),
            available=True)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_object_name_is_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = product.name
        self.assertEqual(str(product), expected_object_name)

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        url = reverse('products:product_detail',
                      args=[product.id, product.slug])
        self.assertEqual(product.get_absolute_url(), url)

    def test_get_rating_returns_average_rating(self):
        product = Product.objects.get(id=1)
        user1 = User.objects.create_user(
            'testuser1',
            'testuser1@test.com',
            'password')
        user2 = User.objects.create_user(
            'testuser2',
            'testuser2@test.com',
            'password')
        review1 = ProductReview.objects.create(
            product=product,
            user=user1,
            content='Test Review 1',
            stars=4)
        review2 = ProductReview.objects.create(
            product=product,
            user=user2,
            content='Test Review 2',
            stars=5)
        # calculate expected average rating
        expected_avg_rating = (review1.stars + review2.stars) / 2.0

        # check the actual average rating
        actual_avg_rating = product.get_rating()

        # assert that the actual average rating matches the expected value
        self.assertEqual(actual_avg_rating, expected_avg_rating)


class ProductReviewModelTest(TestCase):
    """
    Test Product Review Model
    """
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category')
        self.user = User.objects.create(
            username='testuser',
            password='password')
        self.product = Product.objects.create(
            name='Test Product',
            slug='test-product',
            description='Test Description',
            price=10.00,
            category=self.category,
            image_url='https://testurl.com/image.jpg',
            available=True)
        self.review = ProductReview.objects.create(
            product=self.product,
            user=self.user,
            content='Test Review',
            stars=5.0)

    def test_string_representation(self):
        self.assertEqual(
            str(self.review),
            f'{self.user.username} rated 5.0 stars to Test Product')

    def test_review_content(self):
        self.assertEqual(self.review.content, 'Test Review')

    def test_review_stars(self):
        self.assertEqual(self.review.stars, 5.0)

    def test_review_product_relationship(self):
        self.assertEqual(self.review.product, self.product)

    def test_review_user_relationship(self):
        self.assertEqual(self.review.user, self.user)
