# Generated by Django 3.0.2 on 2020-03-28 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0018_auto_20200321_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 28, 10, 21, 17, 331035)),
        ),
    ]
