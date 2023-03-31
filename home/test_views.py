from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User

from .models import FAQ


class HomePageTests(TestCase):
    """
    Test homepage view
    """
    def test_home_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_url_available_by_name(self):
        response = self.client.get(reverse("home:index"))
        self.assertEqual(response.status_code, 200)

    def test_home_template_name_correct(self):
        response = self.client.get(reverse("home:index"))
        self.assertTemplateUsed(response, "home/index.html")

    def test_home_template_content(self):
        response = self.client.get(reverse("home:index"))
        self.assertContains(
            response,
            "Shop Our Collections here")
        self.assertNotContains(response, "Not on the page")


class AboutPageTests(TestCase):
    """
    Test About page view
    """
    def test_about_url_exists_at_correct_location(self):
        response = self.client.get("/pages/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_url_available_by_name(self):
        response = self.client.get(reverse("home:about_view"))
        self.assertEqual(response.status_code, 200)

    def test_about_template_name_correct(self):
        response = self.client.get(reverse("home:about_view"))
        self.assertTemplateUsed(response, "home/about.html")
        self.assertTemplateUsed(response, 'includes/footer.html')

    def test_about_template_content(self):
        response = self.client.get(reverse("home:about_view"))
        self.assertContains(
            response,
            "Welcome to Hand-Crafted Designs")
        self.assertNotContains(response, "Not on the page")


class PrivacyPolicyPageTests(TestCase):
    """
    Test Privacy Policy page view
    """
    def test_privacy_policy_url_exists_at_correct_location(self):
        response = self.client.get("/pages/privacy_policy/")
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_url_available_by_name(self):
        response = self.client.get(reverse("home:privacy_policy"))
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_template_name_correct(self):
        response = self.client.get(reverse("home:privacy_policy"))
        self.assertTemplateUsed(response, "home/privacy_policy.html")
        self.assertTemplateUsed(response, 'includes/footer.html')

    def test_privacy_policy_template_content(self):
        response = self.client.get(reverse("home:privacy_policy"))
        self.assertContains(
            response,
            "Privacy Policy")
        self.assertNotContains(response, "Not on the page")


class FAQPageTests(TestCase):
    """
    Test FAQs page view
    """
    def test_faq_url_exists_at_correct_location(self):
        response = self.client.get("/pages/faq/")
        self.assertEqual(response.status_code, 200)

    def test_faq_url_available_by_name(self):
        response = self.client.get(reverse("home:faq_view"))
        self.assertEqual(response.status_code, 200)

    def test_faq_template_name_correct(self):
        response = self.client.get(reverse("home:faq_view"))
        self.assertTemplateUsed(response, "home/faq.html")
        self.assertTemplateUsed(response, "includes/footer.html")

    def test_faq_template_content(self):
        response = self.client.get(reverse("home:faq_view"))
        self.assertNotContains(response, "Not on the page")


class ContactPageTests(TestCase):
    """
    Test Contact page view
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

    def test_contact_url_exists_at_correct_location(self):
        response = self.client.get("/pages/contact/")
        self.assertEqual(response.status_code, 200)

    def test_contact_url_available_by_name(self):
        response = self.client.get(reverse("home:contact_view"))
        self.assertEqual(response.status_code, 200)

    def test_contact_template_name_correct(self):
        response = self.client.get(reverse("home:contact_view"))
        self.assertTemplateUsed(response, "home/contact.html")

    def test_contact_template_content(self):
        response = self.client.get(reverse("home:contact_view"))
        self.assertNotContains(response, "Not on the page")

    def test_contact_view_with_valid_data(self):
        url = reverse('home:contact_view')
        data = {
            'name': 'testuser',
            'email': 'testuser@email.com',
            'recipient': 'testuser@email.com',
            'content': 'text content',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Email Sent!!")
        self.assertRedirects(response, reverse('products:product_list'))

    def test_contact_view_invalid_data(self):
        url = reverse('home:contact_view')
        data = {
            'name': '', 'email': 'testuser@email.com',
            'recipient': '', 'content': 'text content',
        }
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')
