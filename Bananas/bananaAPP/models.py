import django.utils.timezone
from django.db import models


class Articles(models.Model):  # Посты
    name = models.TextField(default='NULL', max_length='50')
    created_by = models.TextField(default='NULL')
    created_date = models.DateTimeField(default=django.utils.timezone.now(), null=False)
    rank = models.IntegerField(default='0')
    preview = models.TextField(default='NULL')
    text = models.TextField(default='NULL')
    category = models.CharField(default='NULL', max_length=255)


class Feedback(models.Model):  # Обратная связь
    contact = models.CharField(max_length=255, default='None')
    text = models.TextField(default='NULL')
    date = models.DateTimeField(default=django.utils.timezone.now())


class User(models.Model):  # Юзеры
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(default=django.utils.timezone.now())

