# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0004_auto_20150504_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='event',
            field=models.CharField(max_length=500, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 6, 36, 45, 749353), editable=False),
            preserve_default=True,
        ),
    ]
