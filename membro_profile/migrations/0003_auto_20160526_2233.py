# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0002_auto_20160526_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprovantepagamento',
            name='membro',
            field=models.OneToOneField(to='membro_profile.MembroProfile'),
        ),
    ]