""" Cart app model tests """
from django.utils import timezone
from django.test import TestCase

from .models import Discount


class TestDiscountModel(TestCase):
    """ Test the cart app """

    def test_string_method_returns_discount_code(self):
        """ Test Discount model string method returns discount code """
        discount = Discount.objects.create(
            code = 'TESTCODE',
            valid_from = timezone.now(),
            valid_to = timezone.now(),
            amount = 10,
        )
        self.assertEqual(str(discount), 'TESTCODE')
