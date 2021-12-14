""" Tests for the products app's models """
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Product, Category, Review


class TestCategoryModel(TestCase):
    """ Tests the Category model """

    def test_string_method_returns_name(self):
        """ Test string method returns category name """
        category = Category.objects.create(
            name = 'test_category',
            display_name = 'Test Category'
        )
        self.assertEqual(str(category), 'test_category')

    def test_get_display_name_method(self):
        """ Test get display name method returns category display name """
        category = Category.objects.create(
            name = 'test_category',
            display_name = 'Test Category'
        )
        self.assertEqual(category.get_display_name(), 'Test Category')


class TestProductModel(TestCase):
    """ Tests the Product Model """

    def test_string_method_returns_name(self):
        """ Test string method returns product name """
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
        self.assertEqual(str(product), 'Test Product')

    def test_product_calculate_rating(self):
        """ Test product calculate rating method"""
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
        review1 = Review.objects.create(
            product = get_object_or_404(Product, name="Test Product"),
            rating = 1,
            content = 'This is a test review'
        )
        self.assertEqual(product.calculate_rating(), 1.0)
        review2 = Review.objects.create(
            product = get_object_or_404(Product, name="Test Product"),
            rating = 5,
            content = 'This is a second test review'
        )
        self.assertEqual(product.calculate_rating(), 3.0)
        review3 = Review.objects.create(
            product = get_object_or_404(Product, name="Test Product"),
            rating = 3,
            content = 'This is a third test review'
        )
        self.assertEqual(product.calculate_rating(), 3.0)


class TestReviewModel(TestCase):
    """ Tests the Review model """

    def test_string_method_returns_username_and_product(self):
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
        self.assertEqual(user.username + ", " + str(product), 'test, Test Product')
    