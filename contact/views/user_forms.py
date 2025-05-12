from django.shortcuts import render, redirect
from contact.form import RegistrationForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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

def login_view(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, f'Sucessfully logged in. Welcome {user}!')
            return redirect('contact:index')
        
        messages.error(request, 'User or passowrd invalid, please check and try again')
      
    context = {
        'form': form,
        'site_title': 'Login | ',
    }

    return render(
        request,
        'contact/login.html',
        context
    )

def logout_view(request):
    auth.logout(request)

    return redirect('contact:login')

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    context = {
        'form': form,
        'site_title': 'Update User | ',
        }

    if request.method != 'POST':
        context = {
        'form': form,
        'site_title': 'Update User | ',
        }
    
        return render(
            request,
            'contact/register.html',
            context
    )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        context = {
        'form': form,
        'site_title': 'Update User | ',
        }

        return render(
            request,
            'contact/register.html',
            context
    )

    context = {
        'form': form,
        'site_title': 'Update User | ',
    }

    form.save()
    

    return redirect('contact:user_update')
    