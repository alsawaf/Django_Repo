# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=32)),
                ('Last_Name', models.CharField(max_length=32)),
                ('Email', models.EmailField(max_length=124, unique=True)),
            ],
        ),
    ]