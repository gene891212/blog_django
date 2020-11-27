from django.urls import path
from . import views
from view_article.views import PostDetailView

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('<int:pk>', PostDetailView.as_view()),
]