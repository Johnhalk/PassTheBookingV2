from django.test import TestCase
from .models import Client
from property.models import Property

class ClientViewsTestCase(TestCase):

    def test_client_index(self):
        client_1 = Client.objects.create(
            email="John_test@test.com",
            first_name="John",
            last_name="Test"
        )
        resp = self.client.get('/client/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('clients' in resp.context)
        self.assertEqual([client.pk for client in resp.context['clients']], [1])

    def test_client_detail(self):
        client_1 = Client.objects.create(
            email="John_test@test.com",
            first_name="John",
            last_name="Test"
        )
        property_1 = Property.objects.create(
            owner=client_1,
            description="Good for a test",
            location_city="London",
            Address="123 Test Street",
            number_of_bedrooms="2"
        )
        property_2 = Property.objects.create(
            owner=client_1,
            description="Good for a test 2",
            location_city="Bristol",
            Address="12 Test Street",
            number_of_bedrooms="3"
        )
        resp = self.client.get('/client/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('clients' in resp.context)
        self.assertTrue('propertys' in resp.context)
        self.assertEqual(resp.context['clients'].pk, 1)
        properties=Property.objects.all()
        self.assertEqual(properties[0].owner.pk, 1)
        self.assertEqual(properties[1].owner.pk, 1)
