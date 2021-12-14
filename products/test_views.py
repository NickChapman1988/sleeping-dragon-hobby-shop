""" Test products app views """
from django.contrib.auth.models import User

from django.test import TestCase
from django.urls import resolve

from .models import Product, Category, Review


class TestProductsViews(TestCase):
    """ Test products app views """

    def test_get_all_products(self):
        """ Test all products view """
        found = resolve('/products/')
        self.assertEqual(found.url_name, "products")

    def test_get_product_detail(self):
        """ Test for product details view """
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
        found = resolve(f'/products/{product.id}/')
        self.assertEqual(found.url_name, "product_detail")

    def test_get_product_mgmt_page(self):
        """ Test for product management view """
        found = resolve('/products/product_management/')
        self.assertEqual(found.url_name, "product_management")

    def test_get_review_product_page(self):
        """ Test for review product view """
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
            content = 'This is a test review'
        )
        found = resolve(f'/products/review_product/{review.id}/')
        self.assertEqual(found.url_name, "review_product")

    def test_can_add_product(self):
        """ Test for add product view """
        found = resolve('/products/add/')
        self.assertEqual(found.url_name, "add_product")

    def test_can_edit_product(self):
        """ Test for edit product view """
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
        found = resolve(f'/products/edit/{product.id}/')
        self.assertEqual(found.url_name, "edit_product")

    def test_can_delete_product(self):
        """ Test for delete product view """
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
        found = resolve(f'/products/delete/{product.id}/')
        self.assertEqual(found.url_name, "delete_product")

    def test_can_add_category(self):
        """ Test for add category view """
        found = resolve('/products/add_category/')
        self.assertEqual(found.url_name, "add_category")

    def test_can_edit_category(self):
        """ Test for edit category view """
        category = Category.objects.create(
            name = 'test_category',
            display_name = 'Test Category'
        )
        found = resolve(
            f'/products/product_management/edit_category/{category.id}/')
        self.assertEqual(found.url_name, "edit_category")

    def test_can_delete_category(self):
        """ Test for delete category view """
        category = Category.objects.create(
            name = 'test_category',
            display_name = 'Test Category'
        )
        found = resolve(
            f'/products/product_management/delete_category/{category.id}/')
        self.assertEqual(found.url_name, "delete_category")

    def test_can_delete_review(self):
        """ Test for delete review view """
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
        found = resolve(f'/products/delete_review/{review.id}/{user.id}/')
        self.assertEqual(found.url_name, "delete_review")
    