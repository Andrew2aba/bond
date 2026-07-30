from django.conf import settings
from django.db import models
from typing import ClassVar


class Dealer(models.Model):
    STATUS_CHOICES: ClassVar[list] = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    Buisness_Name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wesbsite = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    buisness_email = models.EmailField()
    
    
    def __str__(self):
        return f"{self.Buisness_Name} ({self.status})"