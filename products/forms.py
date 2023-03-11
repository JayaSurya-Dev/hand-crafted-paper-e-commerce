from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('wishlist',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):
    """
    Form for Product Review
    """
    class Meta:
        model = ProductReview
        fields = ('stars', 'content')

    def __init__(self, *args, **kwargs):
        """Remove content label and add placeholder text"""
        super(ProductReviewForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''
        self.fields['content'].widget.attrs['placeholder'] = 'Add review \
here...'
