from django import forms
from homepage.models import *

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.NumberInput(attrs={'class': 'form-control'})
        }