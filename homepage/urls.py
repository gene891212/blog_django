from django.urls import path
from . import views
from view_article.views import *

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('<int:pk>', postview),
]