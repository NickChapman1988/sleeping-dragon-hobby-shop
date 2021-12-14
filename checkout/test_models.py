from decimal import Decimal
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.test import TestCase
from products.models import Product
from cart.models import Discount
from .models import Order, OrderLineItem


class TestOrderModel(TestCase):
    """ Test checkout order model """

    def test_order_str(self):
        """ Test order model string method returns order number """
        order = Order.objects.create(
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            order_total  = 15.00,
            delivery_cost = 2.00,
            grand_total = 17.00,
            stripe_pid = "Test Stripe PID",
        )
        self.assertIsInstance(str(order), str)
        self.assertEqual(len(str(order)), 32)

    def test_generate_order_number(self):
        """ Test order model generates random order number """
        order = Order.objects.create(
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            order_total  = 15.00,
            delivery_cost = 2.00,
            grand_total = 17.00,
            stripe_pid = "Test Stripe PID",
        )
        self.assertIsInstance(order.order_number, str)
        self.assertEqual(len(order.order_number), 32)

    def test_discount_is_applied(self):
        """ Test discount is applied correctly """
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
        Discount.objects.create(
            code = 'TESTCODE',
            valid_from = timezone.now(),
            valid_to = timezone.now(),
            amount = 10,
        )
        product = get_object_or_404(Product, name="Test Product")
        discount = get_object_or_404(Discount, code="TESTCODE")
        order = Order.objects.create(
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            stripe_pid = "Test Stripe PID",
            discount = discount
        )
        orderlineitem = OrderLineItem.objects.create(
            order = order,
            product = product,
            quantity = 60
        )
        # Total of £60, with £6 discount and no delivery
        self.assertEqual(order.grand_total, 54.00)
        self.assertEqual(order.delivery_cost, 0.00)

        orderlineitem.quantity = 100
        orderlineitem.save()

        # New total will be £90.00: £100, discount of £10
        self.assertEqual(order.grand_total, 90.00)

class TestOrderLineItemModel(TestCase):
    """ Test OrderLineItem Model """

    def test_string_method_returns_sku_and_order_number(self):
        """ Test string method returns product sku and order number """
        product = Product.objects.create(
            sku = 'TEST',
            name = 'Test Product',
            description = 'This is a test product',
            stock = 99,
            weight = 1.0,
            length = 1.0,
            width = 1.0,
            height = 1.0,
            price = 1.0,
        )
        order = Order.objects.create(
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            stripe_pid = "Test Stripe PID",
        )
        orderlineitem = OrderLineItem.objects.create(
            order = order,
            product = product,
            quantity = 10,
        )

        self.assertEqual(str(orderlineitem), 
        f'SKU {product.sku} on order {order.order_number}')