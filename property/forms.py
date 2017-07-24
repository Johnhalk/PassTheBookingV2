from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('owner', 'location_city', 'address', 'number_of_bedrooms')
