from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

def index(request):
    contact = Contact.objects.filter(show=True).order_by('-id')
    context = {'contacts': contact,}

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact.objects.
                                       filter(pk=contact_id, show=True))

    if single_contact is None:
        raise Http404('Unable to find contact')

    context = {'contact': single_contact,}

    return render(
        request,
        'contact/contact.html',
        context
    )