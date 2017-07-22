from django.db import models
from functools import partial
from django import forms
import datetime
from property.models import Property
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

class Booking(models.Model):
    property_booking = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_check_in = models.DateField(default=datetime.date.today)
    date_check_out = models.DateField(default=datetime.date.today)
    guest_name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.property_booking)
