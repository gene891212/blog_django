from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *


def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/login')
    return render(request, 'login/register.html', {'form':form})

def sign_in(request):
    form = LoginForm()
    msg = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')  #重新導向到首頁
        else:
            msg = '帳號或密碼錯誤，請重新輸入！'
    context = {
        'form': form,
        'error': msg
        }
    return render(request, 'login/login.html', context)

def log_out(request):
    logout(request)
    return redirect('/login')

def test(request):
    return render(request, 'test.html')