from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bookproperty

def book_property_list(request):
    bookings = Bookproperty.objects.all()
    return render(request, 'book_property/bookproperty_list.html', {'bookings': bookings})

def book_property_detail(request, pk, **kwargs):
    bookings = get_object_or_404(Bookproperty, pk=pk)
    which_property = Bookproperty.objects.filter(property_booking=pk)
    return render(request, 'book_property/bookproperty_detail.html', {'bookings': bookings, 'which_property': which_property})
