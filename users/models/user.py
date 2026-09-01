from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


def current_month_joined():
    """Default 'joined' to the first day of the current month/year."""
    return timezone.now().date().replace(day=1)


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=10, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    joined = models.DateField(default=current_month_joined)
    