# Generated by Django 3.0.2 on 2020-03-03 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0008_auto_20200227_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 3, 18, 49, 32, 509776)),
        ),
    ]