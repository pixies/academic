from django.contrib import admin
from submissao.models import Submissao
class SubmissaoAdmin(admin.ModelAdmin):

    list_display = ('titulo','autor','data_de_criacao','area','status_do_resumo')
# Register your models here.
admin.site.register(Submissao, SubmissaoAdmin)