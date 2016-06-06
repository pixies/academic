# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0006_auto_20160601_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membroprofile',
            name='tipo_de_inscricao',
            field=models.CharField(default=b'estudante', max_length=50, verbose_name=b'tipo de inscri\xc3\xa7\xc3\xa3o', choices=[(b'estudante', b'Estudante de Gradua\xc3\xa7\xc3\xa3o'), (b'estudante-socio', b'Estudante de Gradua\xc3\xa7\xc3\xa3o S\xc3\xb3cio'), (b'estudante-pos', b'Estudante de P\xc3\xb3s-Gradua\xc3\xa7\xc3\xa3o'), (b'estudante-pos-socio', b'Estudante de P\xc3\xb3s-Gradua\xc3\xa7\xc3\xa3o S\xc3\xb3cio'), (b'profi', b'Profissional'), (b'profi-socio', b'Profissional S\xc3\xb3cio')]),
        ),
    ]
