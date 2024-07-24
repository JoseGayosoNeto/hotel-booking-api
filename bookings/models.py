from django.db import models
from hotels.models import Hotel
from rooms.models import Room
from room_services.models import RoomService
from user.models import Guest


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='hotel_bookings')
    guests = models.ManyToManyField(Guest)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='rooms')
    service = models.ForeignKey(RoomService, on_delete=models.PROTECT,
                                related_name='booking_services')
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
        return f'Booking: {self.hotel} - {self.guests} - {self.room}'
