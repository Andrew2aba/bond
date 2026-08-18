from django.contrib import admin

# Register your models here.
from .models import listing
from .models import Vehicle

admin.site.register(listing)
admin.site.register(Vehicle)