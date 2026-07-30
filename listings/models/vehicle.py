from django.db import models


class bodyType(models.TextChoices):
    TRUCK = 'Truck'
    SUV = 'SUV'
    SEDAN = 'Sedan'
    COUPE = 'Coupe'
    MINIVAN = 'Minivan'
    HATCHBACK = 'Hatchback'
    WAGON = 'Wagon'
    
class transmissionType(models.TextChoices):
    AUTOMATIC = 'Automatic'
    MANUAL = 'Manual'


class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    description = models.TextField(blank=True) # Optional field for additional details
    Photo = models.ImageField(upload_to='vehicle_photos/', blank=True, null=True) 
    engine = models.CharField(max_length=255, choices=transmissionType.choices) 
    body_type = models.CharField(max_length=100, choices=bodyType.choices, null=True, blank=True) 
    
    
class Photo(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='vehicle_photos/')
    is_primary = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
   
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    