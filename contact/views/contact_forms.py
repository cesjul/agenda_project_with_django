from typing import Any
from django.shortcuts import render
from contact.form import ContactForm

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