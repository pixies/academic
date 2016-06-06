from django.contrib import admin


from submissao.models import Submissao
# Register your models here.

class SubmissaoAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','area_de_interesse','status_da_submissao']
    search_fields = ['id']
    list_editable = ['status_da_submissao']
    list_filter = ['area_de_interesse']


admin.site.register(Submissao, SubmissaoAdmin)