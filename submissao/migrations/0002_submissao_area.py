# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='area',
            field=models.CharField(default=datetime.date(2016, 6, 1), max_length=200),
            preserve_default=False,
        ),
    ]
