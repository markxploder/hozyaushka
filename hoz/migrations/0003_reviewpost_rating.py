# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoz', '0002_auto_20171205_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewpost',
            name='rating',
            field=models.IntegerField(choices=[('item1', 'item 1'), ('item2', 'item 2')], default=1),
        ),
    ]
