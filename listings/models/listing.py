from django.db import models
from typing import ClassVar
from .vehicle import Vehicle

class listing(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    milage = models.PositiveIntegerField()
    DEAL_STATUS: ClassVar[list] = [
        ('good', 'Good'),
        ('average', 'Average'),
        ('bad', 'Bad'),
    ]
    deal = models.CharField(max_length=10, choices=DEAL_STATUS)

    def __str__(self):
        return self.title