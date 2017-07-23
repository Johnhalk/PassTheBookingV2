from django.test import TestCase
from .models import Client
from .forms import ClientForm

class ClientFormTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_valid_data(self):
        form=ClientForm({
            'email': 'Test@test.com',
            'first_name': 'John',
            'last_name': 'Ashton',
        })
        self.assertTrue(form.is_valid())
        client=form.save()
        self.assertEqual(client.email, 'Test@test.com')
        self.assertEqual(client.first_name, 'John')
        self.assertEqual(client.last_name, 'Ashton')

    def test_blank_data(self):
        form = ClientForm({})
        self.assertFalse(form.is_valid())
