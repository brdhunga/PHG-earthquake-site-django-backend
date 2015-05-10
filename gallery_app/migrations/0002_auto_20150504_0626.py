# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='images',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 6, 26, 44, 687559), editable=False),
            preserve_default=True,
        ),
    ]
