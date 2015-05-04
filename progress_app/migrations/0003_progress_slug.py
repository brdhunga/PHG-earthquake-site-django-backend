# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress_app', '0002_auto_20150502_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='slug',
            field=models.CharField(default='', unique=True, blank=True, max_length=60),
            preserve_default=True,
        ),
    ]
