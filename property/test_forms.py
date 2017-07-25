from django.test import TestCase
from .models import Property
from .forms import PropertyForm

class PropertyFormTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_valid_data(self):
        form=PropertyForm({
            'owner': 2,
            'description': 'Nice place.',
            'location_city': 'Bristol',
            'address': '123 Test Street',
            'number_of_bedrooms': '4',
        })
        self.assertTrue(form.is_valid())
        properties=form.save()
        self.assertEqual(properties.owner.pk, 2)
        self.assertEqual(properties.description, 'Nice place.')
        self.assertEqual(properties.location_city, 'Bristol')
        self.assertEqual(properties.address, '123 Test Street')
        self.assertEqual(properties.number_of_bedrooms, 4)

    def test_blank_data(self):
        form = PropertyForm({})
        self.assertFalse(form.is_valid())
