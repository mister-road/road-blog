# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]