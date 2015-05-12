# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0002_auto_20150427_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='album',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='end_time',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='solo',
            name='start_time',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
    ]
