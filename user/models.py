from django.contrib.auth.models import User
from django.db import models
from hotels.models import Hotel
from roles.models import Role


class CustomUser(User):

    class UserGender(models.IntegerChoices):
        MALE = 1, "Male"
        FEMALE = 2, "Female"
        OTHER = 3, "Other"

    date_of_birthday = models.DateTimeField(null=False, blank=False)
    gender = models.IntegerField(choices=UserGender.choices, default=UserGender.MALE,
                                 null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=70, null=False, blank=False)
    country = models.CharField(max_length=70, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employee(CustomUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='role_employees')
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='hotel_employees')
    salary = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

class Guest(CustomUser):
    passport_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "guest"
        verbose_name_plural = "guests"
