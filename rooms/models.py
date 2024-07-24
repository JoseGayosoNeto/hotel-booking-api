from django.db import models
from room_types.models import RoomType
from hotels.models import Hotel


class Room(models.Model):

    class Status(models.IntegerChoices):
        OCCUPIED = 1, "Occupied"
        AVAILABLE = 2, "Available"
        RESERVED = 3, "Reserved"
        OUT_OF_ORDER = 4, "Out of Order"

    id = models.AutoField(primary_key=True, unique=True, null=False, blank=False)
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT, related_name='rooms')
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='rooms')
    occupancy = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.IntegerField(choices=Status.choices, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room ID:{self.id} Room Type: {self.room_type}"
