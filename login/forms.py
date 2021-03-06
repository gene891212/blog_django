from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'id': 'register_username', 'class': 'login_text'})
    )
    # email = forms.EmailField(
    #     label="電子郵件",
    #     widget=forms.EmailInput(attrs={'class': 'form-control'})
    # )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'id': 'register_password1', 'class': 'login_text'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'id': 'register_password2', 'class': 'login_text'})
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(forms.ModelForm):

    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'login_text', 'placeholder': 'Username'})
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'login_text', 'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')
