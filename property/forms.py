from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('owner',  'description', 'location_city', 'address', 'number_of_bedrooms')
