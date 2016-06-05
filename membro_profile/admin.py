from django.contrib import admin
from membro_profile.models import MembroProfile
# Register your models here.
class MembroProfileAdmin(admin.ModelAdmin):

    list_display = ('user','cpf', 'status_inscricao','tipo_de_inscricao','data_de_cadastro')
    list_filter = ['status_inscricao','tipo_de_inscricao']
    list_editable = ['status_inscricao']

admin.site.register(MembroProfile, MembroProfileAdmin)
#admin.site.register(ComprovantePagamento)
