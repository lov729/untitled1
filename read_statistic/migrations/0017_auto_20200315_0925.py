# Generated by Django 3.0.2 on 2020-03-15 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0016_auto_20200315_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 15, 9, 25, 36, 31994)),
        ),
    ]