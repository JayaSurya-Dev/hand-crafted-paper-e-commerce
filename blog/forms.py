from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    """
    Form for comment
    """
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        """Remove body label and add placeholder text"""
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs['placeholder'] = 'Add comment here...'