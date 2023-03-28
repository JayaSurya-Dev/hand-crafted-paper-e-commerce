from django.test import TestCase
from django.urls import reverse
from home.models import FAQ


class TestFAQModel(TestCase):
    """
    Test FAQ model
    """
    def setUp(self):
        self.faq_1 = FAQ.objects.create(
            question='test question',
            answer='test answer')

    def test_faq_model_str_(self):
        """Test faq model return name"""
        data = self.faq_1
        self.assertEqual(
            data.__str__(), 'test question')
