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
    paginate_by = 30
    ordering = ['-date', '-id']


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'].content = markdown.markdown(
            context['object'].content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        return context