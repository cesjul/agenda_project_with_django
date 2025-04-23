from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator

def create(request):
    
    return render(
        request,
        'contact/create.html',
        
    )