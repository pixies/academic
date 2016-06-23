#-*- encoding: utf-8 -*-

from django.db import models
from membro_profile.models import MembroProfile


# Create your models here.
class Submissao(models.Model):

    titulo = models.CharField(max_length=300, null=True)
    titulo_eng = models.CharField(max_length=300, null=False)
    arquivo = models.FileField(upload_to='resumos/%Y/%m/%d', null=True)

    autor = models.ForeignKey(MembroProfile)

    ESCOLHA_AREA = (
        ('1', "Manejo de água e solo"),
        ('2', "Exploração de espécies agrícolas e nativas"),
        ('3', "Tecnologias na pós - colheita de produtos agrícolas"),
        ('4', "Impactos dos fatores bióticos e abióticos na Produção Vegetal")
    )

    area_de_interesse = models.CharField(
        'Status',
        max_length=1,
        choices=ESCOLHA_AREA,
        default='1',
        blank=True,
    )

    STATUS_DA_SUBMISSAO = (
        ('aguardando', 'Aguardando Revisão'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    )

    status_da_submissao = models.CharField(
        'Status', max_length=11,
        choices=STATUS_DA_SUBMISSAO,
        default='aguardando',
        blank=True,
    )

    def __str__(self):
        return self.titulo