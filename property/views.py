from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Property

def property_list(request):
    propertys = Property.objects.all()
    return render(request, 'property/property_list.html', {'propertys': propertys})

def property_detail(request, pk):
    propertys = get_object_or_404(Property, pk=pk)
    return render(request, 'property/property_detail.html', {'propertys': propertys})
