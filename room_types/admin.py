from django.contrib import admin
from room_types.models import RoomType


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'default_price', 'created_at', 'updated_at',)
    search_fields = ('type_name', 'default_price',)
