from django import forms


class ContactForm(forms.Form):
    """
    Contact form
    """
    name = forms.CharField(label="Your Name", max_length=150)
    email = forms.EmailField(label='Your Email', max_length=150)
    content = forms.CharField(widget=forms.Textarea)
