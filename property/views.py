from django.shortcuts import render, get_object_or_404, redirect
from .models import Property
from .forms import PropertyForm
from book_property.models import Bookproperty

def property_list(request):
    propertys = Property.objects.all()
    return render(request, 'property/property_list.html', {'propertys': propertys})

def property_detail(request, pk):
    propertys = get_object_or_404(Property, pk=pk)
    bookings = Bookproperty.objects.filter(property_booking=pk)
    return render(request, 'property/property_detail.html', {'propertys': propertys, 'bookings': bookings})

def property_edit(request, pk):
    propertys = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=propertys)
        if form.is_valid():
            propertys = form.save(commit=False)
            propertys.save()
            return redirect('property_detail', pk=propertys.pk)
    else:
        form = PropertyForm(instance=propertys)
    return render(request, 'property/property_edit.html', {'form': form})
