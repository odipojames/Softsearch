# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-06-18 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='Task', max_length=50),
        ),
    ]