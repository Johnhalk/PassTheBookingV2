from django.test import TestCase
from .models import Booking
from property.models import Property
from booking.models import Client

class BookingViewsTestCase(TestCase):
    fixtures =['initial_data.json']

    def test_book_property_list(self):
        resp=self.client.get('/booking/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('bookings' in resp.context)
        booking_list=Booking.objects.all()
        self.assertEqual(booking_list[0].property_booking.pk, 1)
        self.assertEqual(booking_list[1].property_booking.pk, 1)
        self.assertEqual(booking_list[2].property_booking.pk, 4)
        self.assertEqual(booking_list[3].property_booking.pk, 3)
        self.assertEqual(booking_list[4].property_booking.pk, 2)


    def test_book_property_detail(self):
        resp=self.client.get('/booking/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('bookings' in resp.context)
        self.assertTrue('which_property' in resp.context)
        booking_list=Booking.objects.all()
        self.assertEqual(booking_list[0].property_booking.pk, 1)
        self.assertEqual(booking_list[1].property_booking.pk, 1)

    def test_book_property_edit(self):
        resp = self.client.get('/booking/1/edit/')
        self.assertEqual(resp.status_code, 200)
