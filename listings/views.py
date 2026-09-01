# Create your views here.
from rest_framework import viewsets
from .models import listing, Vehicle
from .serializers import ListingSerializer, VehicleSerializer
from rest_framework.response import Response

class ListingViewSet(viewsets.ModelViewSet):
    queryset = listing.objects.all()
    serializer_class = ListingSerializer
   

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if (serializer.is_valid(raise_exception=True)): 
            self.perform_create(serializer)
            return Response(serializer.data, status=201)


class vheicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
   
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid(raise_exception=True)): 
            self.perform_create(serializer)
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
       