# Generated by Django 4.2.1 on 2023-10-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Seat_count', models.IntegerField(max_length=4)),
                ('Image', models.ImageField(upload_to='picture')),
                ('Director', models.CharField(max_length=100)),
                ('Actors', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=100)),
            ],
        ),
    ]