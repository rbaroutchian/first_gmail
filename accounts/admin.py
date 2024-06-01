from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class CustomAccountAdmin(UserAdmin):
    model = Account
    list_display = (
        'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active',
    )
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password'),
        }),
        ('Personal info', {
            'fields': ('username', 'first_name', 'last_name', 'phone_number'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2',
                       'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Account, CustomAccountAdmin)
