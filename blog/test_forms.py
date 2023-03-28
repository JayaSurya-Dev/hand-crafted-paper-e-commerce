from django.test import TestCase

from django.contrib.auth.models import User

from .forms import PostForm, CommentForm


class TestPostForm(TestCase):
    """
    Test post form
    """

    def test_empty_fields(self):
        """
        Test post form for empty fields
        """
        form_data = {
            'title': '',
            'content': '',
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
        self.assertEqual(form.errors['content'][0], 'This field is required.')


class TestCommentForm(TestCase):
    """
    Test comment form
    """

    def test_empty_fields(self):
        """
        Test comment form for empty fields
        """
        form = CommentForm(data={
            'body': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_comment_form_is_valid(self):
        """
        Test comment form is valid
        """
        form = CommentForm(data={
            'body': 'test body'
        })
        self.assertTrue(form.is_valid())
