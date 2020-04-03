# Generated by Django 3.0.2 on 2020-03-03 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0008_auto_20200217_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_time']},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='blog_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.blogType'),
        ),
    ]