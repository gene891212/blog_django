from django.shortcuts import render
from homepage.models import Post

# Create your views here.
def create_post(request):
    if request.method == 'POST':
        post = Post(
            username='gene_hsieh',
            title=request.POST.get('title'),
            subtitle=request.POST.get('subtitle').strip(),
            content=request.POST.get('content')
        )
        post.save()
    return render(request, 'write_article/write_article.html')