# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0004_auto_20150713_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday_type',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='is_work',
            field=models.CharField(max_length=3, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
