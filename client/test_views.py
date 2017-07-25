from django.test import TestCase
from .models import Client
from property.models import Property

class ClientViewsTestCase(TestCase):
    fixtures = ['initial_data.json']

    def test_client_list(self):
        resp = self.client.get('/client/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('clients' in resp.context)
        self.assertEqual([client.pk for client in resp.context['clients']], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_client_detail(self):
        resp = self.client.get('/client/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('client' in resp.context)
        self.assertTrue('properties' in resp.context)
        self.assertEqual(resp.context['client'].pk, 1)
        properties=Property.objects.all()
        self.assertEqual(properties[0].owner.pk, 1)
        self.assertEqual(properties[1].owner.pk, 1)

    def test_client_edit(self):
        resp = self.client.get('/client/1/edit/')
        self.assertEqual(resp.status_code, 200)

    def test_client_new(self):
        resp = self.client.get('/client/new/')
        self.assertEqual(resp.status_code, 200)
