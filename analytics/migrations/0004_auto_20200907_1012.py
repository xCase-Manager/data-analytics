# Generated by Django 3.1.1 on 2020-09-07 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20200907_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 10, 12, 11, 132658, tzinfo=utc)),
        ),
    ]
