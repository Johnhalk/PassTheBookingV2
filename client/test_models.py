from django.test import TestCase
from .models import Client

class ClientModelsTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_string_representation(self):
        client=Client.objects.all()
        self.assertEqual(str(client[0]), 'John Lennon')
