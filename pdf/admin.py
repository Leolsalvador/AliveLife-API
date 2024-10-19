from django.contrib import admin
from .models import Files, PDF


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file', 'uploaded_at')
    search_fields = ('id','name', 'uploaded_at')

class PDFAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'file')
    search_fields = ('id', 'text', 'file')

admin.site.register(Files, FileAdmin)
admin.site.register(PDF, PDFAdmin)
