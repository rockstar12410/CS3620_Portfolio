from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username =  form.cleaned_data('username')
            messages.success(request, f'Welcome {username}! You are logged in')
            return redirect('login')
    form = RegistrationForm()
    return render(request, 'users/register.html', {'form':form})