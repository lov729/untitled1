# Generated by Django 3.0.2 on 2020-03-04 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0012_auto_20200303_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 4, 9, 10, 45, 118785)),
        ),
    ]
