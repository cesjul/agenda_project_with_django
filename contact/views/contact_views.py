from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404

def index(request):
    contact = Contact.objects.filter(show=True).order_by('-id')
    contacts_title = 'Contacts |'
    context = {'contacts': contact,
               'site_title': contacts_title,
               }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contact = Contact.objects.filter(show=True) \
                    .filter(Q(first_name__icontains=search_value)|
                            Q(last_name__icontains=search_value) |
                            Q(phone__icontains=search_value)) \
                    .order_by('-id')
    
    if search_value.isdecimal() == True:
        contact = Contact.objects.filter(show=True) \
                    .filter(phone__icontains=search_value) \
                    .order_by('-id')

    if search_value.find('@') != -1:
        contact = Contact.objects.filter(show=True) \
                    .filter(email__icontains=search_value) \
                    .order_by('-id')


    contacts_title = f'Results for {search_value} |'
    context = {'contacts': contact,
               'site_title': contacts_title,
               }

    print(contact.query)

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact.objects.
                                       filter(pk=contact_id, show=True))

    contact_title = f'{single_contact.first_name} {single_contact.last_name} | '

    if single_contact is None:
        raise Http404('Unable to find contact')

    context = {'contact': single_contact,
                'site_title':  contact_title,                   
            }

    return render(
        request,
        'contact/contact.html',
        context
    )