# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='arquivo',
            field=models.FileField(null=True, upload_to=b'resumos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='titulo',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
