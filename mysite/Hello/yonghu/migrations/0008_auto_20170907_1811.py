# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 10:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0007_remove_problem_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usedpoint',
            new_name='mark',
        ),
    ]
