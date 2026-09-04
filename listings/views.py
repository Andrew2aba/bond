# Create your views here.
from rest_framework import viewsets
from .models import listing, Vehicle
from .serializers import ListingSerializer, VehicleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class ListingViewSet(viewsets.ModelViewSet):
    queryset = listing.objects.all()
    serializer_class = ListingSerializer
     # Allow read-only access for unauthenticated users, 
     # but require authentication for write operations
    permission_classes = [IsAuthenticatedOrReadOnly] 


class vehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
     # Allow read-only access for unauthenticated users, 
     # but require authentication for write operations
    permission_classes = [IsAuthenticatedOrReadOnly] 
   