# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0011_auto_20150504_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 9, 7, 27, 415714, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 9, 7, 27, 414629, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
