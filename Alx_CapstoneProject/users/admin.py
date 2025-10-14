from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_vendor", "is_active")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_vendor", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone", "address", "is_vendor")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("phone", "address", "is_vendor")}),
    )


