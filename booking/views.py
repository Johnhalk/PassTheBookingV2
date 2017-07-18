from django.shortcuts import render
from django.utils import timezone
from .models import Client

def client_list(request):
    client = Client.objects.all()
    return render(request, 'booking/client_list.html', {'client': client})
