from django.test import TestCase
from .models import Booking

class BookingModelsTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_string_representation(self):
        bookings=Booking.objects.all()
        self.assertEqual(str(bookings[0]), 'Bort - John Lennon, London')
