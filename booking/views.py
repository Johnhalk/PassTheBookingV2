from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking/booking_detail.html', {'booking': booking})

def booking_new(request):
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form=BookingForm()
        return render(request, 'booking/booking_edit.html', {'form': form})

def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_edit.html', {'form': form})
