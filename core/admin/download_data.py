from django.contrib import admin

from ..models import DownloadData


@admin.register(DownloadData)
class DownloadDataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'actual_date',
    )
