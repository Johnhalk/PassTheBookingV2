from django.test import TestCase
from .models import Property

class PropertyModelsTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_string_representation(self):
        propertyies=Property.objects.all()
        self.assertEqual(str(propertyies[0]), 'John Lennon, London')
