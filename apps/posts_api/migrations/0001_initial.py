# Generated by Django 4.2.4 on 2023-08-27 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts')),
                ('description', models.CharField(max_length=250)),
                ('create_data', models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 27, 10, 23, 7, 922443, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'ordering': ['-create_data'],
            },
        ),
    ]