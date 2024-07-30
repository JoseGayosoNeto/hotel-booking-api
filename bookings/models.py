from django.db import models
from hotels.models import Hotel
from rooms.models import Room
from room_services.models import RoomService
from user.models import Guest


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='hotel_bookings')
    guests = models.ManyToManyField(Guest)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='bookings')
    service = models.ForeignKey(RoomService, on_delete=models.PROTECT,
                                related_name='booking_services', null=True, blank=True)
    booking_scheduled_at = models.DateTimeField(null=False, blank=False)
    arrival_date = models.DateTimeField(null=False, blank=False)
    departure_date = models.DateTimeField(null=False, blank=False)
    num_adults = models.PositiveSmallIntegerField(null=False, blank=False)
    num_children = models.PositiveSmallIntegerField(null=False, blank=False)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    is_active = models.BooleanField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-booking_scheduled_at']

    def __str__(self):
        arrival_date = self.arrival_date.strftime("%m-%d-%Y")
        departure_date = self.departure_date.strftime("%m-%d-%Y")
        guests = ', '.join(f'{guest.first_name} {guest.last_name}' for guest in self.guests.all())
        return f"Booking(Hotel:'{self.hotel.name}', Guests:'{guests}', \
                    Arrival Date:'{arrival_date}', \
                    Departure Date: '{departure_date}'"
