from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPost.as_view(template_name = 'view_article/all_post.html'), name='all_post'),
]