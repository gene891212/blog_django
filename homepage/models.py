from django.db import models

class Post(models.Model):
    username = models.CharField("使用者", max_length=50)
    title = models.TextField(max_length=100)
    # 123