# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0005_membroprofile_status_inscricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resumo', models.TextField()),
                ('autor', models.ForeignKey(to='membro_profile.MembroProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
