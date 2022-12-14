# Generated by Django 4.0.6 on 2022-08-02 07:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_board', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='tags',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
