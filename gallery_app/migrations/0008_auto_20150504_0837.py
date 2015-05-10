# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0007_auto_20150504_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='event',
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 8, 37, 6, 843874, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 8, 37, 6, 843377, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
