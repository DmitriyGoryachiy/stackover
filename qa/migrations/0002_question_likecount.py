# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likecount',
            field=models.IntegerField(default=0),
        ),
    ]
