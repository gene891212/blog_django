from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, 'login/register.html', {'form':form})
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'login/register.html', context)

def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'login/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/login')