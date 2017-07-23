from django.test import TestCase
from .models import Property
from .forms import PropertyForm

class PropertyFormTestCase(TestCase):
    fixtures=['initial_data.json']

    def test_valid_data(self):
        form=PropertyForm({
            'owner': 2,
            'location_city': 'Bristol',
            'Address': '123 Test Street',
            'number_of_bedrooms': '4',
        })
        self.assertTrue(form.is_valid())
        propertys=form.save()
        self.assertEqual(propertys.owner.pk, 2)
        self.assertEqual(propertys.location_city, 'Bristol')
        self.assertEqual(propertys.Address, '123 Test Street')
        self.assertEqual(propertys.number_of_bedrooms, 4)

    def test_blank_data(self):
        form = PropertyForm({})
        self.assertFalse(form.is_valid())
