# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0003_auto_20150504_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 6, 27, 42, 613019)),
            preserve_default=True,
        ),
    ]
