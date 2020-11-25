from django.shortcuts import render
from django.views import generic
# from .model import *
# Create your views here.
# def homepage(request):
#     return render(request, 'index.html', context={pic: ''})


class Homepage(generic.ListView):
    # model =
    def homepage(request):
        return render(request, 'index.html', context={pic: ''})