# Generated by Django 3.1.1 on 2020-09-07 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20200907_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 10, 3, 29, 192772)),
        ),
    ]