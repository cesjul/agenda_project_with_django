from typing import Any
from django.shortcuts import render, redirect
from contact.form import ContactForm

def create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'site_title': 'Create Contact | ',
               'form': form,
               }
        
        if form.is_valid():
            form.save()
            return redirect('contact:create')
        
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