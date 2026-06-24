from django.db import models
from django.conf import settings

class Dealer(models.Model):
    status = [('available', 'Available'),('pending', 'Pending'), ('approved', 'Approved'), 
              ('rejected', 'Rejected'), ('closed', 'Closed')]
    
    Buisness_Name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wesbsite = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    buisness_email = models.EmailField()
    status = models.CharField(max_length=20, choices=status, default='pending')
    
    
    def __str__(self):
        return f"{self.Buisness_Name} ({self.status})"