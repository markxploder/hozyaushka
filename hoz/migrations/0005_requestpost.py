# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoz', '0004_auto_20171207_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=180)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
