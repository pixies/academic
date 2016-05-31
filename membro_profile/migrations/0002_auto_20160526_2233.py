# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprovantepagamento',
            name='comprovante',
            field=models.ImageField(upload_to=b'comprovantes'),
        ),
    ]
