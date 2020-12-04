from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='login'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('test/', views.test, name='test'),
]