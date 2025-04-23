from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', 

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