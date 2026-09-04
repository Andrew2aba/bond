from rest_framework  import serializers
from .models import listing 
from .models import Vehicle


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = '__all__'
        

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
        
