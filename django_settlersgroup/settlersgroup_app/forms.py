from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.utils.html import format_html
from django.contrib.auth.password_validation import password_validators_help_texts
#from django.utils.functional import lazy


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        #fields = ['username', 'name', 'phone_number', 'email', 'street', 
        #'building_number', 'apartament_number', 'city', 'post_code', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']