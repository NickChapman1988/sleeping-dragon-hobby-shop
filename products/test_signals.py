""" Test the Products app's signals """
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.contrib.auth.models import User

from products.models import Product, Review


class TestSignals(TestCase):
    """ Test signals """

    def test_update_rating_on_review(self):
        """ Test rating updates when review added or edited """
        user = User.objects.create(
            username = 'test'
        )
        product = Product.objects.create(
            name = 'Test Product',
            description = 'This is a test product',
            stock = 99,
            weight = 1.0,
            length = 1.0,
            width = 1.0,
            height = 1.0,
            price = 1.0,
        )
        review = Review.objects.create(
            product = product,
            rating = 5,
            content = 'This is a test review',
            user = user
        )
        self.assertEqual(product.rating, 5.0)
        # Change existing rating
        review.rating = 3.0
        review.save()
        self.assertEqual(product.rating, 3.0)
        # Add new rating
        review2 = Review.objects.create(
            product = product,
            rating = 5,
            content = 'This is a second test review',
            user = user
        )
        review2.save()
        self.assertEqual(product.rating, 4.0)

    def test_update_rating_on_review_delete(self):
        """ Test rating updates when review is deleted """
        user = User.objects.create(
            username = 'test'
        )
        product = Product.objects.create(
            name = 'Test Product',
            description = 'This is a test product',
            stock = 99,
            weight = 1.0,
            length = 1.0,
            width = 1.0,
            height = 1.0,
            price = 1.0,
        )
        review = Review.objects.create(
            product = product,
            rating = 3,
            content = 'This is a test review',
            user = user
        )
        review2 = Review.objects.create(
            product = product,
            rating = 5,
            content = 'This is a second test review',
            user = user
        )
        self.assertEqual(product.rating, 4.0)
        review.delete()
        updatedproduct = get_object_or_404(Product, name="Test Product")
        self.assertEqual(updatedproduct.rating, 5.0)
