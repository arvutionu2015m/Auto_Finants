from django.contrib import admin
from .models import UploadedDocument, AnalysisResult

@admin.register(UploadedDocument)
class UploadedDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'filename', 'uploaded_at')
    list_filter = ('user', 'uploaded_at')
    search_fields = ('user__username', 'file')

    def filename(self, obj):
        return obj.file.name.split('/')[-1]

@admin.register(AnalysisResult)
class AnalysisResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'document', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'result_text')
