# Generated by Django 4.2.1 on 2023-10-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='Token',
            field=models.TextField(default='no token'),
        ),
    ]
