from django.test import TestCase
from .models import Booking
from property.models import Property
from client.models import Client

class BookingViewsTestCase(TestCase):
    fixtures =['initial_data.json']

    def test_booking_list(self):
        resp=self.client.get('/booking/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('bookings' in resp.context)
        booking_list=Booking.objects.all()
        self.assertEqual(booking_list[0].property.pk, 1)
        self.assertEqual(booking_list[1].property.pk, 1)
        self.assertEqual(booking_list[2].property.pk, 4)
        self.assertEqual(booking_list[3].property.pk, 3)
        self.assertEqual(booking_list[4].property.pk, 2)


    def test_booking_detail(self):
        resp=self.client.get('/booking/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('booking' in resp.context)
        booking_list=Booking.objects.all()
        self.assertEqual(booking_list[0].property.pk, 1)
        self.assertEqual(booking_list[1].property.pk, 1)

    def test_booking_edit(self):
        resp = self.client.get('/booking/1/edit/')
        self.assertEqual(resp.status_code, 200)

    def test_booking_new(self):
        resp = self.client.get('/booking/new/')
        self.assertEqual(resp.status_code, 200)
