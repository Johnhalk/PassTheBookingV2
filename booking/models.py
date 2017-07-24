from django import forms
from django.db import models

import datetime
import os
import sys
from functools import partial

from property.models import Property

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_check_in = models.DateField(default=datetime.date.today)
    date_check_out = models.DateField(default=datetime.date.today)
    guest_name = models.CharField(max_length=25)

    def __str__(self):
        return self.guest_name + ' - ' + str(self.property)
