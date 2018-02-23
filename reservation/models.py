from django.db import models


class Reservation(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    parking_space_number = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=16)
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
