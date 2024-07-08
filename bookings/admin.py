from django.contrib import admin
from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'service', 'booking_scheduled_at', 'arrival_date',
                    'departure_date', 'num_adults', 'num_children', 'total_price', 'is_active',
                    'created_at', 'updated_at',)

    search_fields = ('hotel__name', 'guests__first_name', 'booking_scheduled_at', 'total_price',
                     'is_active',)
