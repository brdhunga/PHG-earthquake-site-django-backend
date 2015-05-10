# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0009_auto_20150504_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 8, 45, 24, 538950, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 8, 45, 24, 537797, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
