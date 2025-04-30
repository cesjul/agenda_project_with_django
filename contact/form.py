from typing import Any
from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Your first name',
        })
        
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', \
                 'email', 'description', 'category', \
                 'picture',
    
    def clean(self) -> dict[str, Any]:
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name.lower() == last_name.lower(): #type: ignore
            self.add_error(
                'last_name',
                ValidationError(
                'Last name cannot be equals to first name',
                code='invalid')
            )
        return super().clean()
    
    def clean_first_name(self):
        first_name_received = self.cleaned_data.get('first_name')

        if first_name_received == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Invalid name',
                    code='invalid'
            )
            )
        
        return first_name_received