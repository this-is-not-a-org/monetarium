# Generated by Django 3.1.7 on 2021-04-03 07:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]