# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0002_submissao_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='area',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'Area de interesse ', choices=[(b'0', b'Escolha uma op\xc3\xa7\xc3\xa3o'), (b'1', b'Manejo de \xc3\xa1gua e Solo'), (b'2', b'Explora\xc3\xa7\xc3\xa3o de esp\xc3\xa9cies agr\xc3\xadcolas e nativas'), (b'3', b'Tecnologias na po\xcc\x81s - colheita de produtos agr\xc3\xadcolas'), (b'4', b'Impactos dos fatores bi\xc3\xb3ticos e abi\xc3\xb3ticos na Produ\xc3\xa7\xc3\xa3o Vegetal')]),
        ),
    ]
