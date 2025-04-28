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
        fields = 'first_name', 'last_name', 'phone', 

    # def clean(self) -> dict[str, Any]:
    #     self.add_error(
    #         'first_name',
    #         ValidationError(
    #             'Invalid name',
    #             code='invalid'
    #         )
    #     )

    #     return super().clean()