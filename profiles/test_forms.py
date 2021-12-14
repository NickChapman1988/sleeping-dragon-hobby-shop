""" Tests for the Profiles apps forms """

from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """ Tests UserProfileForm """

    def test_fields_in_form_metaclass(self):
        """Test to check fields in form metaclass"""
        form = UserProfileForm()
        form_fields = [field.name for field in form]
        self.assertEqual(form_fields, [
            'default_full_name',
            'default_email',
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country'
            ])

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Tests user field is excluded from form """
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))

    def test_fields_not_required(self):
        """ Test fields are not required """
        form = UserProfileForm({
            'default_full_name' : '',
            'default_email' : '',
            'default_phone_number' : '',
            'default_street_address1' : '',
            'default_street_address2' : '',
            'default_town_or_city ': '',
            'default_county' : '',
            'default_postcode' : '',
            'default_country' : ''
        })
        self.assertTrue(form.is_valid())
