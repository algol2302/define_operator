from django.contrib import admin

from ..models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'parent',
        'name'
    )
