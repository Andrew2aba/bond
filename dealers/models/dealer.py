from django.conf import settings
from django.db import models


class dealStatus(models.Choices):
    AVAILABLE = 'available', 'Available'
    PENDING = 'pending', 'Pending'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'
    CLOSED = 'closed', 'Closed'

class Dealer(models.Model):
    status = models.CharField(max_length=20, choices=dealStatus.choices, default=dealStatus.PENDING)
    Buisness_Name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wesbsite = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    buisness_email = models.EmailField()
    status = models.CharField(max_length=20, choices=status, default='pending')
    
    
    def __str__(self):
        return f"{self.Buisness_Name} ({self.status})"