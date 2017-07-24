from django.shortcuts import render, get_object_or_404, redirect

from .models import Property
from .forms import PropertyForm
from booking.models import Booking


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    bookings = Booking.objects.filter(property=property)
    return render(request, 'property/property_detail.html', {'property': property, 'bookings': bookings})

def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=False)
            property.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property/property_edit.html', {'form': form})
