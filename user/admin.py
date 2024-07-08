from django.contrib import admin
from user.models import CustomUser, Employee, Guest


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'date_of_birthday', 'gender',
                    'phone_number', 'city', 'country', 'is_staff', 'created_at', 'updated_at')

    search_fields = ('email', 'first_name', 'last_name', 'phone_number', 'city', 'country')

@admin.register(Employee)
class EmployeeAdmin(CustomUserAdmin):
    list_display = CustomUserAdmin.list_display + ('role', 'hotel', 'salary',)
    search_fields = CustomUserAdmin.search_fields + ('role__name', 'hotel__name', 'salary',)

@admin.register(Guest)
class GuestAdmin(CustomUserAdmin):
    list_display = CustomUserAdmin.list_display
