#-*- encoding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MembroProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    cpf = models.CharField(max_length=11, blank=True, unique=True)

    data_de_cadastro = models.DateTimeField(auto_now_add=True)

    TIPO_DE_INSCRICAO = (
        ('estudante', 'Estudante de Graduação'),
        ('estudante-socio', 'Estudante de Graduação Sócio'),
        ('estudante-pos', 'Estudante de Pós-Graduação'),
        ('estudante-pos-socio', 'Estudante de Pós-Graduação Sócio'),
        ('profi', 'Profissional'),
        ('profi-socio', 'Profissional Sócio'),
    )
    tipo_de_inscricao = models.CharField('tipo de inscrição',max_length=11,

                                     choices=TIPO_DE_INSCRICAO,
                                     default='estudante')

    STATUS_DE_INSCRICAO = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    )

    status_inscricao = models.CharField('Status', max_length=11,
                                         choices=STATUS_DE_INSCRICAO,
                                         default='inativo',
                                         blank=True,
                                        )

    def __unicode__(self):
        return self.user.first_name


class ComprovantePagamento(models.Model):
    comprovante = models.ImageField(upload_to='comprovantes')
    membro = models.OneToOneField(MembroProfile)

    def __unicode__(self):
        return self.membro