""" Cart app tests """
from django.urls import resolve
from django.shortcuts import get_object_or_404
from django.test import TestCase
from products.models import Product


class TestCartViews(TestCase):
    """ Test the cart app views """

    def test_resolve_view_cart(self):
        """ Resolve the view cart view """
        found = resolve('/cart/')
        self.assertEqual(found.url_name, "view_cart")

    def test_resolve_add_to_cart(self):
        """ Test add to cart view """
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
        product = get_object_or_404(Product, name='Test Product')
        found = resolve(f'/cart/add/{product.id}/')
        self.assertEqual(found.url_name, "add_to_cart")

    def test_resolve_adjust_cart(self):
        """ Test adjust cart view """
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
        product = get_object_or_404(Product, name='Test Product')
        found = resolve(f'/cart/adjust/{product.id}/')
        self.assertEqual(found.url_name, "adjust_cart")

    def test_resolve_remove_from_cart(self):
        """ Test remove from cart view """
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
        product = get_object_or_404(Product, name='Test Product')
        found = resolve(f'/cart/remove/{product.id}/')
        self.assertEqual(found.url_name, "remove_from_cart")

    def test_discount_apply(self):
        """ Test discount apply view """
        found = resolve('/cart/discount_apply/')
        self.assertEqual(found.url_name, "discount_apply")

    def test_cancel_discount(self):
        """ Test cancel discount view """
        found = resolve('/cart/cancel_discount/')
        self.assertEqual(found.url_name, "cancel_discount")
