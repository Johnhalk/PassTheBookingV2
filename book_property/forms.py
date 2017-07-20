from django import forms
from .models import Bookproperty

class BookpropertyForm(forms.ModelForm):

    class Meta:
        model = Bookproperty
        fields = ('property_booking', 'date_check_in', 'date_check_out', 'guest_name')
