from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView

class BookingList(ListView):
    model = Booking
    context_object_name = 'bookings'

class BookingDetail(DetailView):
    model = Booking
    context_object_name = 'booking'

class CreateBooking(CreateView):
    model = Booking
    fields = ['property', 'date_check_in', 'date_check_out', 'guest_name']
    template_name = 'booking/booking_edit.html'
    success_url = '/booking/'

class EditBooking(UpdateView):
    model = Booking
    fields = ['property', 'date_check_in', 'date_check_out', 'guest_name']
    template_name = 'booking/booking_edit.html'
    success_url = '/booking/'
