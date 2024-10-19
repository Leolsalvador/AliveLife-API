from django.contrib import admin
from .models import Diagnosis


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('diagnosis', 'Medical', 'patient', 'approved')
    search_fields = ('diagnosis', 'Medical', 'patient', 'approved')
    list_filter = ('diagnosis', 'Medical', 'patient', 'approved')


admin.site.register(Diagnosis, DiagnosisAdmin)
