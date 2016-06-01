# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0004_submissao_data_de_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='titulo',
            field=models.CharField(default=datetime.date(2016, 6, 1), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submissao',
            name='titulo_eng',
            field=models.CharField(default=datetime.date(2016, 6, 1), max_length=300, blank=True),
            preserve_default=False,
        ),
    ]
