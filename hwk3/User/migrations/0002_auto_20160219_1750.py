# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secret_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srt_title', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
        migrations.AddField(
            model_name='secret_message',
            name='srt_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Person'),
        ),
    ]
