# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0002_auto_20150710_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_work',
        ),
        migrations.RemoveField(
            model_name='member',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='member',
            name='qq',
        ),
        migrations.RemoveField(
            model_name='member',
            name='wechat',
        ),
    ]
