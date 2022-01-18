import django.utils.timezone
from django.db import models


class Articles(models.Model):  # Посты
    name = models.TextField(default='None', null=False, max_length='50')
    created_by = models.TextField(default='None')
    created_date = models.DateTimeField(default=django.utils.timezone.now(), null=False)
    rank = models.IntegerField(default='0', null=False)
    preview = models.TextField(default='None', null=False)
    text = models.TextField(default='None', null=False)
    category = models.CharField(default='None', max_length=255)


class Feedback(models.Model):  # Обратная связь
    contact = models.CharField(max_length=255, default='None')
    text = models.TextField(default='None', null=False)
    date = models.DateTimeField(default=django.utils.timezone.now())


class User(models.Model):  # Юзеры
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(default=django.utils.timezone.now())

