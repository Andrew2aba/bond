# Create your views here.
from rest_framework import viewsets
from .models import listing, Vehicle
from .serializers import ListingSerializer, VehicleSerializer
from rest_framework.response import Response

class ListingViewSet(viewsets.ModelViewSet):
    queryset = listing.objects.all()
    serializer_class = ListingSerializer
   


class vehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
   