# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=300)),
                ('titulo_eng', models.CharField(max_length=300)),
                ('arquivo', models.FileField(upload_to=b'resumos/%Y/%m/%d')),
                ('area_de_interesse', models.CharField(default=b'1', max_length=b'1', verbose_name=b'Status', blank=True, choices=[(b'1', b'Manejo de \xc3\xa1gua e solo'), (b'2', b'Explora\xc3\xa7\xc3\xa3o de esp\xc3\xa9cies agr\xc3\xadcolas e nativas'), (b'3', b'Tecnologias na po\xcc\x81s - colheita de produtos agr\xc3\xadcolas'), (b'4', b'Impactos dos fatores bi\xc3\xb3ticos e abi\xc3\xb3ticos na Produ\xc3\xa7\xc3\xa3o Vegetal')])),
                ('status_da_submissao', models.CharField(default=b'aguardando', max_length=11, verbose_name=b'Status', blank=True, choices=[(b'aguardando', b'Aguardando Revis\xc3\xa3o'), (b'aprovado', b'Aprovado'), (b'rejeitado', b'Rejeitado')])),
                ('autor', models.ForeignKey(to='membro_profile.MembroProfile')),
            ],
        ),
    ]
