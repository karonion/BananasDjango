import django.utils.timezone
from django.db import models


# Посты
class Articles(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=django.utils.timezone.now, null=False)
    preview = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='downloads', verbose_name='Image preview')

    def __str__(self):
        return self.title


# Обратная связь
class Feedback(models.Model):
    contact = models.CharField(max_length=255, default='NULL')
    text = models.TextField(default='NULL')
    date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.contact

