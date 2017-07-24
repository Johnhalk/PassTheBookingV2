from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from .models import Client
from .forms import ClientForm
from property.models import Property

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})

def client_detail(request, pk, **kwargs):
    client = get_object_or_404(Client, pk=pk)
    properties = Property.objects.filter(owner=client)
    return render(request, 'client/client_detail.html', {'client': client, 'properties': properties})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    print client
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.clients = request.user
            client.date_joined = timezone.now()
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
        return render(request, 'client/client_edit.html', {'form': form})
