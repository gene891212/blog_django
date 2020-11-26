from django.shortcuts import render
from django.views import generic
from .models import *
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Homepage(generic.ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.all().order_by('-date')