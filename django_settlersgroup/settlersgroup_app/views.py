from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import JobEmployee
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
#from django.core.mail import EmailMessage

def home(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('settlersgroup-home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})