from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='帳號',
        widget=forms.TextInput()
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(),
    )

class Meta:
    model = User
    fields = ('username', 'email')

class LoginForm(forms.Form):
    username = forms.CharField(
        label='帳號',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )