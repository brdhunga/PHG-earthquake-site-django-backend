# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0005_auto_20150504_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 5, 4, 6, 42, 46, 349211, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
