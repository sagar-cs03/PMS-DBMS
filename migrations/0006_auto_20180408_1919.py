# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmsApp', '0005_auto_20180408_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='ApplicatioId',
            new_name='ApplicationId',
        ),
    ]