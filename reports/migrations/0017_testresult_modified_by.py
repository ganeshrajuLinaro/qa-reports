# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 18:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0016_auto_20160310_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
