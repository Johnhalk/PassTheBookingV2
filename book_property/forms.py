from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('property_booking', 'date_check_in', 'date_check_out', 'guest_name')
