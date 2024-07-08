from django.contrib import admin
from roles.models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at',)
    search_fields = ('name',)
