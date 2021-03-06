# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User'),
        ),
    ]
