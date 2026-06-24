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

class Photo(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='vehicle_photos/')
    is_primary = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    

    class Meta:
        ordering = ['order']