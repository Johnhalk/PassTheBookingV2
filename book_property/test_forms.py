from django.test import TestCase
from .models import Booking
import datetime
from .forms import BookingForm

class BookingFormTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_valid_data(self):
        form=BookingForm({
            'property_booking': 2,
            'date_check_in': '2017-08-15',
            'date_check_out': '2017-09-24',
            'guest_name': 'Richard',
        })
        self.assertTrue(form.is_valid())
        booking=form.save()
        self.assertEqual(booking.property_booking.pk, 2)
        self.assertEqual(booking.date_check_in, datetime.date(2017, 8, 15))
        self.assertEqual(booking.date_check_out, datetime.date(2017, 9, 24))
        self.assertEqual(booking.guest_name, 'Richard')
