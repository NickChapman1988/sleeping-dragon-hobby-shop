""" Checkout app views tests """
from django.test import TestCase
from django.urls import resolve

from .models import Order


class TestCheckoutViews(TestCase):
    """ Test checkout app views """

    def test_resolve_checkout_view(self):
        """Test resolving checkout view"""
        found = resolve('/checkout/')
        self.assertEqual(found.url_name, "checkout")

    def test_resolve_checkout_success_view(self):
        """Test resolving checkout success view"""
        order = Order.objects.create(
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            order_total = 15.00,
            delivery_cost = 2.00,
            grand_total = 17.00,
            stripe_pid = "Test Stripe PID",
        )
        found = resolve(f'/checkout/checkout_success/{order.order_number}')
        self.assertEqual(found.url_name, "checkout_success")

    def test_resolve_wh(self):
        """Test resolving webhook handler view"""
        found = resolve('/checkout/wh/')
        self.assertEqual(found.url_name, "webhook")

    def test_resolve_cache_checkout(self):
        """Test resolving cache checkout data view"""
        found = resolve('/checkout/cache_checkout_data/')
        self.assertEqual(found.url_name, "cache_checkout_data")

    def test_get_checkout_success(self):
        """Test get checkout success view"""
        order = Order.objects.create(
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            order_total = 15.00,
            delivery_cost = 2.00,
            grand_total = 17.00,
            stripe_pid = "Test Stripe PID",
        )
        url = f'/checkout/checkout_success/{order.order_number}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
