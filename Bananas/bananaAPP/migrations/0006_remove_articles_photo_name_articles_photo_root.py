# Generated by Django 4.0.1 on 2022-01-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bananaAPP', '0005_articles_photo_name_alter_articles_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='photo_name',
        ),
        migrations.AddField(
            model_name='articles',
            name='photo_root',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]
