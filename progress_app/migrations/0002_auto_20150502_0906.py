# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='created_at',
            field=models.DateTimeField(editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='progress',
            name='updated_at',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
