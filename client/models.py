from django.db import models
from django.utils import timezone


class Client(models.Model):
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    email = models.EmailField(('email address'), max_length=254, unique=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
