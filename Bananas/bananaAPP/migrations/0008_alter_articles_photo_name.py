# Generated by Django 4.0.1 on 2022-01-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bananaAPP', '0007_remove_articles_photo_root_articles_photo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='photo_name',
            field=models.CharField(default='no', max_length=255),
        ),
    ]
