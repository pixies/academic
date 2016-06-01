# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0003_auto_20160601_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='data_de_criacao',
            field=models.DateTimeField(default=datetime.date(2016, 6, 1), verbose_name=b'data de criacao', auto_now_add=True),
            preserve_default=False,
        ),
    ]
