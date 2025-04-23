from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator

def index(request):
    contact = Contact.objects.filter(show=True).order_by('-id')
    contacts_title = 'Contacts |'
    
    number_of_itens = request.GET.get('number-of-itens')

    if number_of_itens == None or number_of_itens == '' \
        or number_of_itens.isdecimal() == False:
        number_of_itens = 10

    if int(number_of_itens) > 20:
        number_of_itens = 10
    
    if int(number_of_itens) <= 10:
        number_of_itens = 10

    paginator = Paginator(contact, number_of_itens)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,
               'site_title': contacts_title,
               'number_of_itens_': number_of_itens,
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

    number_of_itens = request.GET.get('number-of-itens')

    if number_of_itens == None or number_of_itens == '' \
        or number_of_itens.isdecimal() == False:
        number_of_itens = 10

    if int(number_of_itens) > 20:
        number_of_itens = 10
    
    if int(number_of_itens) <= 10:
        number_of_itens = 10

    paginator = Paginator(contact, number_of_itens)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contacts_title = f'Results for {search_value} |'
    context = {'page_obj': page_obj,
               'site_title': contacts_title,
               'search_value': search_value,
               'number_of_itens_': number_of_itens,
               }

    if contact.exists() == False:
        return noresult(request, search_value)

    return render(
        request,
        'contact/index.html',
        context
    )

def noresult(request, search):

    context = {'search': search,
               'site_title': 'No results |'}

    return render(
        request,
        'contact/noresult.html',
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