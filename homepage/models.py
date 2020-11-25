from django.db import models

class Post(models.Model):
    username = models.CharField("使用者", max_length=50)