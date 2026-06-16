from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50, blank=True) # Optional field for vehicle color
    description = models.TextField(blank=True) # Optional field for additional details
    Photo = models.ImageField(upload_to='vehicle_photos/', blank=True, null=True) # Optional field for vehicle photo
    engine = models.CharField(max_length=255, blank=True) # Optional field for engine details
    
    

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
