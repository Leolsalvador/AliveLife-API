from django.contrib import admin
from .models import Files, PDF


class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'uploaded_at')
    search_fields = ('name', 'uploaded_at')

class PDFAdmin(admin.ModelAdmin):
    list_display = ('text', 'file')
    search_fields = ('text', 'file')

admin.site.register(Files, FileAdmin)
admin.site.register(PDF, PDFAdmin)
