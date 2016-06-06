# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0001_initial'),
        ('membro_profile', '0007_auto_20160602_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='membroprofile',
            name='arquivo',
            field=models.ForeignKey(to='submissao.Submissao', null=True),
        ),
    ]
