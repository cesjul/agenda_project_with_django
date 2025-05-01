from django.shortcuts import render
from contact.form import RegistrationForm

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    context = {
        'form': form,
        'site_title': 'Create User | ',
    }

    return render(
        request,
        'contact/register.html',
        context
    )