from django.test import TestCase

from .forms import BookingForm
from .models import Booking

import datetime


class BookingFormTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_valid_data(self):
        form=BookingForm({
            'property': 2,
            'date_check_in': '2017-08-15',
            'date_check_out': '2017-09-24',
            'guest_name': 'Richard',
        })
        self.assertTrue(form.is_valid())
        booking=form.save()
        self.assertEqual(booking.property.pk, 2)
        self.assertEqual(booking.date_check_in, datetime.date(2017, 8, 15))
        self.assertEqual(booking.date_check_out, datetime.date(2017, 9, 24))
        self.assertEqual(booking.guest_name, 'Richard')

    def test_blank_data(self):
        form = BookingForm({})
        self.assertFalse(form.is_valid())
