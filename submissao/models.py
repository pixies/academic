#-*- encoding: utf-8 -*-
from django.db import models
from membro_profile.models import MembroProfile

# Create your models here.
class Submissao(models.Model):
    titulo = models.CharField(max_length=300)
    titulo_eng = models.CharField(max_length=300, blank=True)
    resumo = models.TextField()
    autor = models.ForeignKey(MembroProfile)
    data_de_criacao = models.DateTimeField('data de criacao', auto_now_add=True)

    ESCOLHA_AREA = (
        ('0', 'Escolha uma opção'),
        ('1', 'Manejo de água e Solo'),
        ('2', 'Exploração de espécies agrícolas e nativas'),
        ('3', 'Tecnologias na pós - colheita de produtos agrícolas'),
        ('4', 'Impactos dos fatores bióticos e abióticos na Produção Vegetal')
    )

    area = models.CharField(
        'Area de interesse ', max_length=1,
        choices=ESCOLHA_AREA,
        default='0',
        blank=False,
    )

    ESCOLHA_STATUS = (
        ('0', 'Aguardando revisão'),
        ('1', 'Em revisão'),
        ('2', 'Aguardando correções'),
        ('3', 'Aprovado'),
        ('4', 'Regeitado')
    )

    status_do_resumo = models.CharField(
        'Status do Resumo', max_length=1,
        choices=ESCOLHA_STATUS,
        default='0',
        blank=True,
    )

    def __unicode__(self):
        return self.titulo