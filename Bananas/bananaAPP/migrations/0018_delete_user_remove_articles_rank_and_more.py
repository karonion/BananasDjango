# Generated by Django 4.0.1 on 2022-02-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bananaAPP', '0017_articles_dislikes_articles_likes_alter_articles_rank_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='rank',
        ),
        migrations.AlterField(
            model_name='articles',
            name='created_by',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AlterField(
            model_name='articles',
            name='preview',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
