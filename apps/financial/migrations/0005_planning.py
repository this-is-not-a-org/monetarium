# Generated by Django 3.1.7 on 2021-04-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0004_auto_20210330_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=650)),
                ('init_date', models.DateField()),
                ('final_date', models.DateField()),
            ],
        ),
    ]