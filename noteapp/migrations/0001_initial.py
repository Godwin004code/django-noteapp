# Generated by Django 4.1.1 on 2022-09-29 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2022, 9, 29, 14, 34, 9, 60838))),
            ],
        ),
    ]
