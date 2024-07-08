from django.contrib import admin
from hotels.models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'postal_code', 'city', 'country',
                    'number_of_rooms', 'phone_number', 'star_rating', 'created_at',
                    'updated_at',)
    search_fields = ('name', 'postal_code', 'city', 'country', 'number_of_rooms',
                     'phone_number', 'star_rating',)
