# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='stream',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subject.Stream'),
            preserve_default=False,
        ),
    ]
