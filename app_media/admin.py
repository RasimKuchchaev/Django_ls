from django.contrib import admin
from app_media.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "create_at")


admin.site.register(File, FileAdmin)