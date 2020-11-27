from django.shortcuts import render
from django.views import generic
from homepage.models import *
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AllPost(generic.ListView):
    model = Post
    template_name = 'view_article/all_post.html'
    def get_queryset(self):
        return Post.objects.all().order_by('-date')

class PostDetailView(generic.DetailView):
    model = Post
    def post_detail_view(request, pk):
        self.model.objects.get(id=pk)

    