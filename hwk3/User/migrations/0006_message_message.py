# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 15:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.CharField(default=datetime.datetime(2016, 2, 22, 15, 1, 11, 357337, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
