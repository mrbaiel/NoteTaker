# note/core/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BasicUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BasicUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

    search_fields = ('email', 'first_name', 'last_name', 'username')
    readonly_fields = ('last_login', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal Info',
            {'fields': ('first_name', 'last_name', 'email')}
        ),
        (
            'Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined')}
        ),
    )
