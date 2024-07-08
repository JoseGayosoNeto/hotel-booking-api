from django.contrib import admin
from rooms.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_type', 'hotel', 'occupancy', 'status','created_at',
                    'updated_at',)
    search_fields = ('room_type__type_name', 'hotel__name', 'occupancy', 'status',)
