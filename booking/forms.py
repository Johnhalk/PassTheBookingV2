from django import forms
from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('clients', 'email', 'first_name', 'last_name')
