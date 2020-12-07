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

# class RegisterForm(UserCreationForm):
#     username = forms.CharField(
#         label='帳號',
#         widget=forms.TextInput()
#     )

#     email = forms.EmailField(
#         label="電子郵件",
#         widget=forms.EmailInput(),
#     )

# class Meta:
#     model = User
#     fields = ('username', 'email')

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         label='帳號',
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     password = forms.CharField(
#         label="密碼",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )