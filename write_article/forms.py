from django import forms
from homepage.models import *

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitle'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'content': forms.Textarea(attrs={'hidden': ''})
        }