# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20170915_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('org', '培训机构'), ('personal', '个人'), ('college', '高校')], default='org', max_length=20, verbose_name='机构类别'),
        ),
    ]