# Generated by Django 5.1 on 2024-11-02 05:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at'),
        ),
    ]