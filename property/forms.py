from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('owner', 'location_city', 'Address', 'number_of_bedrooms')
