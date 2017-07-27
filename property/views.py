from django.shortcuts import render, get_object_or_404, redirect

from .models import Property
from .forms import PropertyForm
from booking.models import Booking
from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView


class PropertyList(ListView):
    model = Property
    context_object_name = 'properties'

class PropertyDetail(DetailView):
    model = Property
    context_object_name = 'property'

class CreateProperty(FormView):
    template_name = 'property/property_edit.html'
    form_class = PropertyForm
    success_url = '/property/'

class EditProperty(FormView):
    template_name = 'property/property_edit.html'
    form_class = PropertyForm
    success_url = '/property/'
