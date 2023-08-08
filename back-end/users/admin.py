from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    UserAdmin class
    overrides base user admin properties 
    """
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': (
            'national_code', 'phone_number',
            'phone_number_verified', 'email_verified', 'role')}),
    )

    list_display = [
        'username', 'email',
        'last_name', 'is_staff',
        "is_active", 'national_code',
        'phone_number', 'phone_number_verified',
        'email_verified', 'role'
    ]
