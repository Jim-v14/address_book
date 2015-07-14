# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0003_auto_20150712_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('managername', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='qq',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='wechat',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
