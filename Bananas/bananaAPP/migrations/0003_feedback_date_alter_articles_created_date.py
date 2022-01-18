# Generated by Django 4.0.1 on 2022-01-18 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bananaAPP', '0002_feedback_alter_articles_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 17, 57, 43, 671980, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 17, 57, 43, 671980, tzinfo=utc)),
        ),
    ]
