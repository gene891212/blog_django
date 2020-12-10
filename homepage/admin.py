from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date')
    fields = [('title', 'subtitle', 'content'), 'username', 'image']