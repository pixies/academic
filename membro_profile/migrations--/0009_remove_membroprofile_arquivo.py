# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membro_profile', '0008_membroprofile_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membroprofile',
            name='arquivo',
        ),
    ]
