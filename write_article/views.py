from django.shortcuts import render

# Create your views here.
def create_post(request):
    return render(request, 'write_article/write_article.html')