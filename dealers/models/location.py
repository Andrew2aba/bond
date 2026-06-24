from django.db import models
from django.conf import settings

class DealerLocation (models.Model):
    dealer = models.OneToOneField('dealers.Dealer', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='USA')  # Default to USA, can be changed if needed

    def __str__(self):
        return f"{self.dealer} Location"