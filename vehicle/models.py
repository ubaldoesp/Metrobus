from django.db import models

# Create your models here.
 
# Create your models here.

class Vehicle(models.Model):
    
    class Relation(models.IntegerChoices):
        No = 0
        Yes = 2   
        
    vehicle_label = models.IntegerField(null=True)
    vehicle_current_status = models.IntegerField(default=1)
    position_latitude = models.DecimalField(max_digits=10,decimal_places=7,null=True)
    position_longitude= models.DecimalField(max_digits=10,decimal_places=8,null=True)
    geographic_point= models.CharField(max_length=100)
    position_speed= models.IntegerField(default=0)
    position_odometer=models.IntegerField(default=0)
    trip_id= models.BigIntegerField(null=True)
    trip_schedule_relationship = models.IntegerField(choices=Relation.choices)
    trip_route = models.IntegerField(null=True)
    trip_start_date = models.IntegerField(null=True)
    town_hall = models.CharField(max_length=50)
    date_creation= models.DateTimeField(auto_now=True)
    date_updated= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.vehicle_label