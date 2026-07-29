from django.contrib import admin
from .models import Dealer

# import class not module 
# Register your models here.
admin.site.register(Dealer)