from django.contrib import admin

from user.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    EmployeeCreationForm,
    EmployeeChangeForm,
    GuestCreationForm,
    GuestChangeForm
)
from user.models import (
        CustomUser,
        Employee,
        Guest,
    )


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('id', 'email', 'is_staff', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('email', 'is_active', 'is_staff',)
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'city', 'country',)
    ordering = ("email",)

@admin.register(Employee)
class EmployeeAdmin(CustomUserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    list_display = CustomUserAdmin.list_display + ('role', 'hotel', 'salary',)
    list_filter = ('email', 'is_active',)
    search_fields = CustomUserAdmin.search_fields + ('role__name', 'hotel__name', 'salary',)

@admin.register(Guest)
class GuestAdmin(CustomUserAdmin):
    add_form = GuestCreationForm
    form = GuestChangeForm
    list_display = CustomUserAdmin.list_display
    list_filter = ('email', 'is_active',)
    search_fields = ('email', 'hotel', 'role',)
