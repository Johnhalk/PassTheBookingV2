from django.test import TestCase

class HomeViewTestCase(TestCase):

    def test_home_list(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code, 200)
