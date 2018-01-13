# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='village',
            name='x',
        ),
        migrations.RemoveField(
            model_name='village',
            name='y',
        ),
        migrations.AddField(
            model_name='village',
            name='postoffice',
            field=models.CharField(default=' ', max_length=500, verbose_name='postoffice'),
        ),
        migrations.AddField(
            model_name='village',
            name='shortest',
            field=models.CharField(default=' ', max_length=500, verbose_name='shortest'),
        ),
        migrations.AddField(
            model_name='village',
            name='village40',
            field=models.CharField(default=' ', max_length=5000, verbose_name='village40'),
        ),
        migrations.AlterField(
            model_name='village',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
