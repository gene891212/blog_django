from django.shortcuts import render
from django.views import generic
from .models import *
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Homepage(generic.ListView):
    model = Post
    # def homepage(request):
    #     return render(request, 'index.html', context={pic: self.hi})
    def get_queryset(self):
        return Post.objects.all().order_by('-date')