from django.contrib import admin
from .models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'created_at', 'updated_at')
    search_fields = ('sender__username', 'recipient', 'subject')  # برای جستجو بر اساس نام کاربری
    list_filter = ('created_at', 'updated_at')


admin.site.register(Email, EmailAdmin)
