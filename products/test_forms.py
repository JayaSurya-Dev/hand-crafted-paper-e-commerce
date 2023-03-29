from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from products.models import Category, Product, ProductReview
from products.forms import ProductForm, ProductReviewForm


class TestProductForm(TestCase):
    """
    Test Product form
    """
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.image_file = SimpleUploadedFile(
            'test_image.png', b'content', content_type='image/png')

    def test_product_form_valid_data(self):
        form_data = {
            'name': 'Test Product',
            'description': 'A test product',
            'price': '10.99',
            'category': self.category.id,
        }
        form = ProductForm(data=form_data, files={'image': self.image_file})

    def test_product_form_invalid_data(self):
        form_data = {
            'name': '',
            'description': '',
            'price': 'invalid',
            'category': self.category.id,
        }
        form = ProductForm(data=form_data, files={'image': self.image_file})
        self.assertFalse(form.is_valid())


class TestProductReviewForm(TestCase):
    """
    Test Product Review form
    """
    def test_review_form_valid_data(self):
        form_data = {
            'stars': 5,
            'content': 'This is a great product!',
        }
        form = ProductReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_data(self):
        form_data = {
            'stars': 6,
            'content': '',
        }
        form = ProductReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
