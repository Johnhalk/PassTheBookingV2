from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm

def book_property_list(request):
    bookings = Booking.objects.all()
    return render(request, 'book_property/bookproperty_list.html', {'bookings': bookings})

def book_property_detail(request, pk):
    bookings = get_object_or_404(Booking, pk=pk)
    which_property = Booking.objects.filter(property_booking=pk)
    return render(request, 'book_property/bookproperty_detail.html', {'bookings': bookings, 'which_property': which_property})

def book_property_edit(request, pk):
    bookings = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=bookings)
        if form.is_valid():
            bookings = form.save(commit=False)
            bookings.save()
            return redirect('bookproperty_detail', pk=bookings.pk)
    else:
        form = BookingForm(instance=bookings)
    return render(request, 'book_property/bookproperty_edit.html', {'form': form})
