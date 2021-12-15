""" Test the checkout app forms """
from django.test import TestCase

from .forms import OrderForm


class TestOrderForm(TestCase):
    """ Test the OrderForm """

    def test_fields_in_form_metaclass(self):
        """Test to check fields in form metaclass"""
        form = OrderForm()
        form_fields = [field.name for field in form]
        self.assertEqual(form_fields, ['full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county', ])

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Test fields are explicit in form metaclass """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        ))

    def test_fields_are_not_required(self):
        """ Test non-required fields """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'street_address2': '',
            'town_or_city': 'test',
            'postcode': '',
            'country': 'GB',
            'county': '',
        })
        self.assertTrue(form.is_valid())

    def test_name_field_is_required(self):
        """ Test name field is required """
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'street_address2': 'test',
            'town_or_city': 'test',
            'postcode': 'test',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_email_field_is_required(self):
        """ Test email field is required """
        form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'street_address2': 'test',
            'town_or_city': 'test',
            'postcode': 'test',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_phone_number_field_is_required(self):
        """ Test phone number field is required """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': 'test',
            'street_address2': 'test',
            'town_or_city': 'test',
            'postcode': 'test',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

    def test_street_address1_field_is_required(self):
        """ Test street address1 field is required """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': '',
            'street_address2': 'test',
            'town_or_city': 'test',
            'postcode': 'test',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_field_is_required(self):
        """ Test town or city field is required """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'street_address2': 'test',
            'town_or_city': '',
            'postcode': 'test',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')

    def test_country_field_is_required(self):
        """ Test country field is required """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'test',
            'street_address2': 'test',
            'town_or_city': 'test',
            'postcode': 'test',
            'country': '',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')
