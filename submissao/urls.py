from django.conf.urls import url
from submissao.views import listar_submissao, adcionar_submissao, editar_submissao, deletar_submissao, detalhes_submissao
from django.contrib import admin

urlpatterns = [
    url(r'^$', listar_submissao),
    url(r'^adcionar/$', adcionar_submissao),
    url(r'^editar/$', editar_submissao),
    url(r'^listar/$', listar_submissao),
    url(r'^detalhes/$', detalhes_submissao),
    url(r'^deletar/$', deletar_submissao),
]
