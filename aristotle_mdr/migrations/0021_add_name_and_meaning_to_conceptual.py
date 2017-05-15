# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-10 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr', '0020_add_uuids'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valuemeaning',
            old_name='meaning',
            new_name='name',
        ),
        migrations.AddField(
            model_name='valuemeaning',
            name='definition',
            field=models.TextField(blank=True, help_text='The semantic definition of a possible value', null=True),
        ),
    ]