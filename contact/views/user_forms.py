from django.shortcuts import render, redirect
from contact.form import RegistrationForm
from django.contrib import messages

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'User sucessfully created')
            return redirect('contact:index')
    

    context = {
        'form': form,
        'site_title': 'Create User | ',
    }


    return render(
        request,
        'contact/register.html',
        context
    )