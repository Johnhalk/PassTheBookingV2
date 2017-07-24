from django import forms
from django.db import models

from functools import partial
import sys, os

from client.models import Client

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

class Property(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    location_city = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    number_of_bedrooms = models.IntegerField()

    def __str__(self):
        return str(self.owner) + ', ' + self.location_city
