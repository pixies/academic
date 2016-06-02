from membro_profile.models import MembroProfile, ComprovantePagamento
from django.contrib import admin
from membro_profile.models import MembroProfile, ComprovantePagamento
# Register your models here.
class MembroProfileAdmin(admin.ModelAdmin):

    list_display = ('user','cpf', 'status_inscricao','tipo_de_inscricao','data_de_cadastro')

admin.site.register(MembroProfile, MembroProfileAdmin)
#admin.site.register(ComprovantePagamento)
