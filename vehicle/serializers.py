from pyexpat import model
from rest_framework.serializers import ModelSerializer

from .models import Vehicle

class VehicleSerializer(ModelSerializer):
    
    class Meta:
        model = Vehicle
        fields ='__all__'

class TownhallSerializer(ModelSerializer):
    
    class Meta:
        model = Vehicle
        fields = ['town_hall']