# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0005_membroprofile_status_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membroprofile',
            name='cpf',
            field=models.CharField(unique=True, max_length=11, blank=True),
        ),
    ]
