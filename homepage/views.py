from django.shortcuts import render
from django.views import generic
from .models import *
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template

import markdown
# Create your views here.

class Homepage(generic.ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.all().order_by('-date')[:5]

class PostDetailView(generic.DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'].content = markdown.markdown(
            context['post'].content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        return context