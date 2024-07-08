from django.contrib import admin
from room_services.models import RoomService


@admin.register(RoomService)
class RoomServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'scheduled_at', 'cost_price', 'created_at', 'updated_at',)
    search_fields = ('service_name', 'scheduled_at', 'cost_price',)
