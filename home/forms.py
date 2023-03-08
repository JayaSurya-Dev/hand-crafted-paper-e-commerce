from django import forms


class ContactForm(forms.Form):
    """
    Contact form
    """
    name = forms.CharField(label="Your Name", max_length=150)
    email = forms.EmailField(label='Your Email', max_length=150)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ('name', 'email', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email': 'Your Email',
            'content': 'Your Content...'

        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
