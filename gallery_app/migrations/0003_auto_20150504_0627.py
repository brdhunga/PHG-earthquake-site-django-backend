# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_auto_20150504_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 6, 27, 20, 918505), editable=False),
            preserve_default=True,
        ),
    ]
