# Generated by Django 2.0 on 2018-01-23 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_app', '0002_auto_20180123_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
