from django.shortcuts import render, redirect
from homepage.models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm
# Create your views here.

@login_required(login_url='/login/')
def create_post(request):
    form = PostModelForm()

    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'write_article/write_article.html', context)
