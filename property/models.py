from django.db import models
from django.utils import timezone
from functools import partial
from django import forms
from booking.models import Client
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
DateInput = partial(forms.DateInput, {'class': 'datepicker'})



class Property(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    location_city = models.CharField(max_length=100)
    Address = models.CharField(max_length=150, unique=True)
    number_of_bedrooms = models.IntegerField()
    start_date_availability = forms.DateField(widget=DateInput())
    end_date_availability = forms.DateField(widget=DateInput())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.location_city
