from django.contrib import admin

from ..models import PhoneNumber


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'abc',
        'start_number', 'end_number'
    )
