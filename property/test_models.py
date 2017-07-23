from django.test import TestCase
from .models import Property

class PropertyModelsTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_string_representation(self):
        propertys=Property.objects.all()
        self.assertEqual(str(propertys[0]), 'London')
