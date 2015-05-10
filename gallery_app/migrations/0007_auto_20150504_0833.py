# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0006_auto_20150504_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 5, 4, 8, 33, 22, 617326, tzinfo=utc), editable=False)),
                ('images', models.ManyToManyField(related_name='event_gallery', to='gallery_app.Image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 8, 33, 22, 616802, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
