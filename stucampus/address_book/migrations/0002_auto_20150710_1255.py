# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='department',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dormitory',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_work',
            field=models.CharField(max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_num_long',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_num_short',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.FileField(upload_to=b'./upload/', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='qq',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='stuID',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='wechat',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
