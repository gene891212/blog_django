from django import forms
from homepage.models import *

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['username', 'title', 'subtitle', 'image', 'content']
        widgets = {
            'username': forms.TextInput(attrs={'hidden': ''}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitle'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'content': forms.Textarea(attrs={'': ''})
        }