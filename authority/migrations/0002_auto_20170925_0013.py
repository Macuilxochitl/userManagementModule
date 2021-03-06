# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-24 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='actCode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='isActivated',
            field=models.BooleanField(default=False),
        ),
    ]
