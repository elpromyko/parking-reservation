from django.db import models
from parking_building import ParkingSlot


class Reservation(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
