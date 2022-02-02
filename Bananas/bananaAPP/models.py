import django.utils.timezone
from django.db import models


# Посты
class Articles(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.CharField(default='NULL', max_length=255)
    created_date = models.DateTimeField(default=django.utils.timezone.now, null=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    preview = models.CharField(max_length=255)
    text = models.TextField()
    category = models.CharField(default='NULL', max_length=255)
    image = models.ImageField(upload_to='downloads')

    def __str__(self):
        return self.title


# Обратная связь
class Feedback(models.Model):
    contact = models.CharField(max_length=255, default='NULL')
    text = models.TextField(default='NULL')
    date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.contact

