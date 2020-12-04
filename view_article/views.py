from django.shortcuts import render, get_object_or_404
from django.views import generic
from homepage.models import *
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

import markdown
# Create your views here.

class AllPost(generic.ListView):
    model = Post
    template_name = 'view_article/all_post.html'
    def get_queryset(self):
        return Post.objects.all().order_by('-date')

class PostDetailView(generic.DetailView):
    model = Post
    def post_detail_view(request, pk):
        post_detail = self.model.get_object_or_404(Post, id=pk)
        post_detail.content = markdown.markdown(
            post_detail.content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        print(post_detail)
        return render(request, 'homepage/post_detail.html', {'post': post_detail})

def postview(request, pk):
    model = Post
    post_detail = get_object_or_404(Post, id=pk)
    post_detail.content = markdown.markdown(
        post_detail.content,
        extensions=[
            # 'markdown.extensions.abbr',
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    return render(request, 'homepage/post_detail.html', {'post': post_detail})
    