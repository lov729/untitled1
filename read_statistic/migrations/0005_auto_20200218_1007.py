# Generated by Django 3.0.2 on 2020-02-18 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0004_auto_20200217_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 18, 10, 7, 11, 296999)),
        ),
    ]
