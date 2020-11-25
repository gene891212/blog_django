from django.shortcuts import render
from django.views import generic
from .models import *
from datetime import datetime

# Create your views here.

class Homepage(generic.ListView):
    model = Post
    now = model.datetime.timestamp
    hi = datetime.fromtimestamp(now)

    def homepage(request):
        return render(request, 'index.html', context={pic: self.hi})