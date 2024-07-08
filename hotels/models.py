from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    number_of_rooms = models.PositiveSmallIntegerField(default=1, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    star_rating = models.IntegerField(null=False, blank=False, validators=[
        MinValueValidator(0, message="Hotel cannot be less than 0 stars"),
        MaxValueValidator(5, message="Hotel cannot be higher than 5 stars"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
