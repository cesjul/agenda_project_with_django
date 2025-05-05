from typing import Any
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django import forms

class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', \
                 'email', 'description', 'category', \
                 'picture',
    
    def clean(self) -> dict[str, Any]:
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name.lower() == last_name.lower(): #type: ignore
            self.add_error(
                'last_name',
                ValidationError(
                'Last name cannot be equals to first name',
                code='invalid')
            )
        return super().clean()
    
    def clean_first_name(self):
        first_name_received = self.cleaned_data.get('first_name')

        if first_name_received == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Invalid name',
                    code='invalid'
            )
            )
        
        return first_name_received
    
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=2,

    )

    last_name = forms.CharField(
        required=True,
        min_length=2,
        
    )

    email = forms.EmailField(
        required=True
    )


    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'This email adress has already been registered, please, insert a new one',
                    code='invalid'
                )
            )

        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
         min_length=2,
         max_length=30,
         required=True,
         help_text='Required.',
         error_messages={
             'min_length': 'Please, add more than 2 letters.'
         }
     )
    last_name = forms.CharField(
         min_length=2,
         max_length=30,
         required=True,
         help_text='Required.'
     )
 
    password1 = forms.CharField(
         label="Password",
         strip=False,
         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
         help_text=password_validation.password_validators_help_text_html(),
         required=False,
     )
 
    password2 = forms.CharField(
         label="Confirm Password",
         strip=False,
         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
         help_text='Use the same password as before.',
         required=False,
     )
 
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )
    
    def clean(self) -> dict[str, Any]:
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error('password2',
                    ValidationError('Passwords must be equal')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                'email',
                ValidationError(
                    'This email adress has already been registered, please, insert a new one',
                    code='invalid'
                )
            )

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as error:
                self.add_error('password1', ValidationError(error))
