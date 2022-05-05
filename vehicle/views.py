from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.decorators import api_view
from vehicle.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehicle
# Create your views here.
class VehicleViewSet(APIView):
    
    def get(self,request, format=None):
        vehicles=Vehicle.objects.filter(vehicle_current_status=2)
        serializer= VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
    
    
     
class DetailVehicleGenericView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class TownhallGenericView(ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['town_hall']     


@api_view(['GET'])
def disponibles(request):
    if request.method == 'GET':
        lista_alcaldias= Vehicle.objects.filter(vehicle_current_status=2).values('town_hall').distinct()
        serializer = TownhallSerializer(lista_alcaldias, many=True)
        return Response(serializer.data)