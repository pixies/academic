# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0003_auto_20160526_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='membroprofile',
            name='data_de_cadastro',
            field=models.DateTimeField(default=datetime.date(2016, 5, 26), auto_now_add=True),
            preserve_default=False,
        ),
    ]
