# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=300, default='', blank=True)),
                ('contribution', models.DecimalField(decimal_places=2, default=0.0, blank=True, max_digits=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
