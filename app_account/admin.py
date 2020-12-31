from django.contrib import admin
from .models import User, Email, Address
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.utils.translation import ugettext_lazy as _


class EmailAdmin(admin.TabularInline):
    model = Email
    verbose_name = _('Email')
    verbose_name_plural = _('Emails')
    readonly_fields = ('subject', 'to', 'body')
    extra = 0


class AddressAdmin(admin.TabularInline):
    model = Address
    verbose_name = _('Address')
    verbose_name_plural = _('Addresses')
    readonly_fields = ('city', 'postal_code', 'street', 'alley', 'no')
    extra = 0


@admin.register(User)
class UserAdmin(UserBaseAdmin):
    ordering = ('email',)
    list_display = ('profile_picture', 'email', 'is_staff', 'is_active')
    list_per_page = 10
    list_display_links = ('email',)
    search_fields = ('email',)
    add_fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password1', 'password2')}),
    )
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Personal Option', {'fields': ('avatar',)}),
        ('Status', {'fields': ('is_staff', 'is_active', 'is_seller', 'groups')})
    )
    inlines = (
        EmailAdmin,
        AddressAdmin,
    )
