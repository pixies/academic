# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprovantePagamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comprovante', models.FileField(upload_to=b'comprovantes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembroProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('cpf', models.CharField(max_length=11, blank=True)),
                ('tipo_de_inscricao', models.CharField(default=b'estudante', max_length=11, verbose_name=b'tipo de inscri\xc3\xa7\xc3\xa3o', choices=[(b'estudante', b'Estudante de Gradua\xc3\xa7\xc3\xa3o'), (b'estudante-socio', b'Estudante de Gradua\xc3\xa7\xc3\xa3o S\xc3\xb3cio'), (b'estudante-pos', b'Estudante de P\xc3\xb3s-Gradua\xc3\xa7\xc3\xa3o'), (b'estudante-pos-socio', b'Estudante de P\xc3\xb3s-Gradua\xc3\xa7\xc3\xa3o S\xc3\xb3cio'), (b'profi', b'Profissional'), (b'profi-socio', b'Profissional S\xc3\xb3cio')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comprovantepagamento',
            name='membro',
            field=models.ForeignKey(to='membro_profile.MembroProfile'),
            preserve_default=True,
        ),
    ]
