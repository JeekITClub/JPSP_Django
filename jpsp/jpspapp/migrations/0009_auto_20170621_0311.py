# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jpspapp', '0008_auto_20170621_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='ClubId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='ClubId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club'),
        ),
        migrations.AlterField(
            model_name='post',
            name='CludId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club'),
        ),
    ]
