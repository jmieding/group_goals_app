# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='f',
            new_name='friday',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='m',
            new_name='monday',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='s',
            new_name='saturday',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='su',
            new_name='sunday',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='t',
            new_name='thursday',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='th',
            new_name='tuesday',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='w',
            new_name='wednesday',
        ),
    ]
