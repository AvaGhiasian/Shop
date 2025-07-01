from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from .forms import StoreUserCreationForm, StoreUserChangeForm


# Register your models here.


@admin.register(StoreUser)
class ShopUserAdmin(UserAdmin):
    ordering = ['phone']
    add_form = StoreUserCreationForm
    form = StoreUserChangeForm
    model = StoreUser
    list_display = ['phone', 'first_name', 'last_name', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'address',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'address',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
    )
