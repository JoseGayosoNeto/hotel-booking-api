from django.db import models


class RoomType(models.Model):
    type_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    default_price = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False)
    img = models.ImageField(upload_to='room_types_imgs/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['type_name']

    def __str__(self):
        return str(self.type_name)
