# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_preview_html'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preview_html',
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt_html',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
    ]