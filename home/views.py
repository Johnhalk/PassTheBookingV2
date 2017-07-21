from django.shortcuts import render, get_object_or_404, redirect
from property.models import Property
from book_property.models import Booking
from booking.models import Client


def home_list(request):
    return render(request, 'home/home_list.html', {})
