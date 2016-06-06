# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0004_membroprofile_data_de_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='membroprofile',
            name='status_inscricao',
            field=models.CharField(default=b'inativo', max_length=11, verbose_name=b'Status', blank=True, choices=[(b'ativo', b'Ativo'), (b'inativo', b'Inativo')]),
            preserve_default=True,
        ),
    ]
