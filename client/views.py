from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from .models import Client
from .forms import ClientForm
from property.models import Property
from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView

class ClientList(ListView):
    model = Client
    context_object_name = 'clients'

class ClientDetail(DetailView):
    model = Client
    context_object_name = 'client'

class CreateClient(CreateView):
    template_name = 'client/client_edit.html'
    form_class = ClientForm
    success_url = '/client/'

class EditClient(UpdateView):
    template_name = 'client/client_edit.html'
    form_class = ClientForm
    success_url = '/client/'
