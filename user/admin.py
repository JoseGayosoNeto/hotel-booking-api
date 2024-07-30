from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

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
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', 'email', 'is_staff', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('email', 'is_active', 'is_staff',)
    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'city', 'country',)
    ordering = ("email",)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number',
                                      'address', 'postal_code', 'city', 'country',
                                      'date_of_birthday', 'gender',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'address',
                       'postal_code', 'city', 'country', 'date_of_birthday', 'gender',
                       'password1', 'password2'),
        }),
    )

@admin.register(Employee)
class EmployeeAdmin(CustomUserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee
    list_display = CustomUserAdmin.list_display + ('role', 'hotel', 'salary',)
    list_filter = ('email', 'is_active',)
    search_fields = CustomUserAdmin.search_fields + ('role__name', 'hotel__name', 'salary',)
    fieldsets = CustomUserAdmin.fieldsets + (
        ('Job Info', {'fields': ('role', 'hotel', 'salary',)}),
    )
    add_fieldsets = CustomUserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('role', 'hotel', 'salary'),
        }),
    )

@admin.register(Guest)
class GuestAdmin(CustomUserAdmin):
    add_form = GuestCreationForm
    form = GuestChangeForm
    model = Guest
    list_display = CustomUserAdmin.list_display
    list_filter = ('email', 'is_active',)
    search_fields = ('email', 'passport_number',)
    fieldsets = CustomUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('passport_number',)}),
    )
    add_fieldsets = CustomUserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('passport_number',),
        }),
    )
