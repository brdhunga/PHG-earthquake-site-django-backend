# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0010_auto_20150504_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover_image',
            field=models.URLField(blank=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 9, 2, 55, 646693, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventname',
            name='name',
            field=models.CharField(blank=True, max_length=500, default='', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 9, 2, 55, 645547, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
