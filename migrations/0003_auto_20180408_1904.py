# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pmsApp', '0002_auto_20180408_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='ApplicantId',
        ),
        migrations.RemoveField(
            model_name='status',
            name='ApplicantId',
        ),
        migrations.AddField(
            model_name='documents',
            name='ApplicationId',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pmsApp.Application'),
        ),
        migrations.AddField(
            model_name='status',
            name='ApplicatioId',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pmsApp.Application'),
        ),
    ]
