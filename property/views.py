from django.shortcuts import render
from .models import Property

def property_list(request):
    propertys = Property.objects.all()
    return render(request, 'property/property_list.html', {'propertys': propertys})
