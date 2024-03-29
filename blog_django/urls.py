"""blog_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf.urls.static import static
from django.conf import settings

import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/homepage/')),
    path('homepage/', include('homepage.urls'), name='homepage'),
    path('login/', include('login.urls'), name='login'),
    path('create_post/', include('write_article.urls'), name='create-article'),
    path('profile/', include('persional_page.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
