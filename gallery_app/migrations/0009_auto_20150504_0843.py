# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0008_auto_20150504_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventName',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='event',
            field=models.ManyToManyField(related_name='event_name', to='gallery_app.EventName'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 8, 43, 3, 228967, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.OneToOneField(related_name='main_event', to='gallery_app.EventName'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 8, 43, 3, 227641, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
