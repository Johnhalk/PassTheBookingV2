from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from property.models import Property

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'booking/client_list.html', {'clients': clients})

def client_detail(request, pk, **kwargs):
    clients = get_object_or_404(Client, pk=pk)
    propertys = Property.objects.filter(owner=pk)
    return render(request, 'booking/client_detail.html', {'clients': clients, 'propertys': propertys})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.clients = request.user
            client.date_joined = timezone.now()
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
        return render(request, 'booking/client_edit.html', {'form': form})
