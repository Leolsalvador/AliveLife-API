from django.contrib import admin
from .models import Medico, Paciente

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'data_nascimento', 'crm', 'uf_crm')
    search_fields = ('nome', 'email', 'cpf', 'crm')
    list_filter = ('uf_crm',)
    ordering = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('user', 'nome', 'email', 'cpf', 'data_nascimento', 'crm', 'uf_crm')
        }),
    )

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome', 'email', 'cpf', 'data_nascimento')
    search_fields = ('nome', 'email', 'cpf')
    ordering = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('user', 'nome', 'email', 'cpf', 'data_nascimento')
        }),
    )

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
