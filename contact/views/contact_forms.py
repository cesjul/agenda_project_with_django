from typing import Any
from django.shortcuts import render
from contact.models import Contact
from django.core.exceptions import ValidationError

from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', 

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Invalid name',
                code='invalid'
            )
        )

        return super().clean()

def create(request):

    if request.method == 'POST':
        context = {'site_title': 'Create Contact | ',
               'form': ContactForm(request.POST),
               }
        
        return render(
        request,
        'contact/create.html',
        context
    )

    context = {'site_title': 'Create Contact | ',
               'form': ContactForm(),
               }


    return render(
        request,
        'contact/create.html',
        context
    )