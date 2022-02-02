# Generated by Django 4.0.1 on 2022-01-29 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bananaAPP', '0011_remove_articles_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default='0')),
                ('dislikes', models.IntegerField(default='0')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bananaAPP.articles')),
            ],
        ),
    ]