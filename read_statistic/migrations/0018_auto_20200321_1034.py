# Generated by Django 3.0.2 on 2020-03-21 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0017_auto_20200315_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 21, 10, 34, 4, 731981)),
        ),
    ]
