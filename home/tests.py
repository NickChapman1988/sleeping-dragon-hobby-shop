""" Home app tests """
from django.test import TestCase


class TestHomeViews(TestCase):
    """ Test Home app views """
    def test_landing_page(self):
        """ Tests loading the landing page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        