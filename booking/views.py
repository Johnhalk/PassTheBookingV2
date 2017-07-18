from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Client
from .forms import ClientForm


def client_list(request):
    clients = Client.objects.filter(date_joined__lte=timezone.now())
    return render(request, 'booking/client_list.html', {'clients': clients})

def client_detail(request, pk):
    clients = get_object_or_404(Client, pk=pk)
    return render(request, 'booking/client_detail.html', {'clients': clients})

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.clients = request.user
            client.email = request.user
            client.first_name = request.user
            client.last_name = request.user
            client.date_joined = timezone.now()
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
        return render(request, 'booking/client_edit.html', {'form': form})


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.clients = request.user
            client.email = request.user
            client.first_name = request.user
            client.last_name = request.user
            client.date_joined = timezone.now()
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
        return render(request, 'booking/client_edit.html', {'form': form})
