from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Client


def client_list(request):
    clients = Client.objects.filter(date_joined__lte=timezone.now())
    return render(request, 'booking/client_list.html', {'clients': clients})

def client_detail(request, pk):
    clients = get_object_or_404(Client, pk=pk)
    return render(request, 'booking/client_detail.html', {'clients': clients})
