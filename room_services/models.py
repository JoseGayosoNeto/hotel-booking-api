from django.db import models


class RoomService(models.Model):

    class ServicesNames(models.IntegerChoices):
        SPA = 1, "Spa"
        RESTAURANT = 2, "Restaurant"
        BAR = 3, "Bar"
        HOTEL_SHUTTLE = 4, "Hotel Shuttle"

    service_name = models.IntegerField(choices=ServicesNames.choices,
                                    default=ServicesNames.SPA, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    scheduled_at = models.DateTimeField(null=False, blank=False)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.service_name)
