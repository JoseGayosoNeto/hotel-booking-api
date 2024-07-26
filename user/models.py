from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from hotels.models import Hotel
from roles.models import Role

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class UserGender(models.IntegerChoices):
        MALE = 1, "Male"
        FEMALE = 2, "Female"
        OTHER = 3, "Other"

    email= models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    date_of_birthday = models.DateTimeField(null=True, blank=True)
    gender = models.IntegerField(choices=UserGender.choices, default=UserGender.MALE,
                                 null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=70, null=False, blank=False)
    country = models.CharField(max_length=70, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Custom Users"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'


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
