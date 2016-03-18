# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0017_testresult_modified_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=64)),
                ('remote_id', models.CharField(max_length=256)),
                ('remote_url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bugs', to='reports.TestResult')),
            ],
        ),
    ]
