from django.db import models

class Post(models.Model):
    username = models.CharField("使用者", max_length=50)
    title = models.TextField('標題', max_length=100)
    subtitle = models.TextField('副標', max_length=100, blank=True)
    content = models.TextField('內文')
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title
    