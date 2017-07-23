from django.test import TestCase
from .models import Property
from booking.models import Client

class PropertyViewsTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_property_list(self):
        resp=self.client.get('/property/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('propertys' in resp.context)
        property_list=Property.objects.all()
        self.assertEqual(property_list[0].owner.pk, 1)
        self.assertEqual(property_list[1].owner.pk, 1)
        self.assertEqual(property_list[2].owner.pk, 2)
        self.assertEqual(property_list[3].owner.pk, 3)
        self.assertEqual(property_list[4].owner.pk, 4)
        self.assertEqual(property_list[5].owner.pk, 4)

    def test_property_detail(self):
        resp=self.client.get('/property/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('propertys' in resp.context)
        self.assertTrue('bookings' in resp.context)
        property_list=Property.objects.all()
        self.assertEqual(property_list[0].owner.pk, 1)
        self.assertEqual(property_list[1].owner.pk, 1)

    def test_property_edit(self):
        resp=self.client.get('/property/1/edit/')
        self.assertEqual(resp.status_code, 200)
