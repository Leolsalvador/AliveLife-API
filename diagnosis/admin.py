from django.contrib import admin
from .models import Diagnosis


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('diagnosis', 'Medical', 'patient')
    search_fields = ('diagnosis', 'Medical', 'patient')
    list_filter = ('diagnosis', 'Medical', 'patient')


admin.site.register(Diagnosis, DiagnosisAdmin)
