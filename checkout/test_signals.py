""" Tests for the Checkout app signals """
from django.shortcuts import get_object_or_404
from django.test import TestCase
from products.models import Product
from .models import Order, OrderLineItem


class TestCheckoutSignals(TestCase):
    """ Test checkout signals """

    def test_order_lineitems_update_total(self):
        """ Test order total updates when lineitems added or updated """
        Product.objects.create(
            name = 'Test Product',
            description = 'This is a test product',
            stock = 99,
            weight = 1.0,
            length = 1.0,
            width = 1.0,
            height = 1.0,
            price = 1.0,
        )

        product = get_object_or_404(Product, name="Test Product")
        order = Order.objects.create(
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            stripe_pid = "Test Stripe PID",
        )
        # Add 50 items at £1 each, to reach free delivery threshold
        orderlineitem = OrderLineItem.objects.create(
            order = order,
            product = product,
            quantity = 50,
        )
        # Total will be £50, with no delivery fee
        self.assertEqual(order.grand_total, 50.00)
        OrderLineItem.objects.create(
            order = order,
            product = product,
            quantity = 5,
        )
        # Total will be £55
        self.assertEqual(order.grand_total, 55.00)
        orderlineitem.delete()
        # Total will be £5 plus 50p delivery
        self.assertEqual(order.grand_total, 5.50)
