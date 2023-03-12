from django import forms

from django_summernote.widgets import SummernoteWidget

from products.widgets import CustomClearableFileInput

from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for posts
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'featured_image',
            'status',
        )
        widgets = {
            'content': SummernoteWidget(),
        }

    featured_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """Remove labels and add placeholder text"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'title',
            'content': 'Add content here...',
            'featured_image': 'Featured Image',
            'status': 'Status',
        }
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = \
                'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class CommentForm(forms.ModelForm):
    """
    Form for comment
    """
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        """Remove body label and add placeholder text"""
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs['placeholder'] = 'Add comment here...'
