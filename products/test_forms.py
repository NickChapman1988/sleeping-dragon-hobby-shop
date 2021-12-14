""" Tests forms in the products app """
from django.test import TestCase
from .forms import ProductForm, CategoryForm, ReviewForm


class TestProductForm(TestCase):
    """ Tests the product form """

    def test_product_name_is_required(self):
        """ Test name field is required """
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_stock_is_required(self):
        """ Test stock field is required """
        form = ProductForm({'stock': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('stock', form.errors.keys())
        self.assertEqual(form.errors['stock'][0], 'This field is required.')

    def test_product_description_is_required(self):
        """ Test description field is required """
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_product_weight_is_required(self):
        """ Test weight field is required """
        form = ProductForm({'weight': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('weight', form.errors.keys())
        self.assertEqual(form.errors['weight'][0], 'This field is required.')

    def test_product_length_is_required(self):
        """ Test length field is required """
        form = ProductForm({'length': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('length', form.errors.keys())
        self.assertEqual(form.errors['length'][0], 'This field is required.')

    def test_product_width_is_required(self):
        """ Test width field is required """
        form = ProductForm({'width': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('width', form.errors.keys())
        self.assertEqual(form.errors['width'][0], 'This field is required.')

    def test_product_height_is_required(self):
        """ Test name height is required """
        form = ProductForm({'height': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('height', form.errors.keys())
        self.assertEqual(form.errors['height'][0], 'This field is required.')

    def test_product_price_is_required(self):
        """ Test price field is required """
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_product_fields_not_required(self):
        """ Test other form fields are not required """
        form = ProductForm({
            'name': 'Test Product',
            'description': 'This is a Test Product',
            'stock': '99',
            'weight': '1.0',
            'length': '1.0',
            'width': '1.0',
            'height': '1.0',
            'price': '1.0',
        })
        self.assertTrue(form.is_valid())


class TestCategoryForm(TestCase):
    """ Tests the category form """

    def test_category_name_is_required(self):
        """ Test name field is required """
        form = CategoryForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_category_display_name_not_required(self):
        """ Test display name field is not required """
        form = CategoryForm({'name': 'Test Category'})
        self.assertTrue(form.is_valid())


class TestReviewForm(TestCase):
    """ Tests the review form """

    def test_content_field_is_required(self):
        """ Test review content field is required """
        form = ReviewForm({
            'content': '',
            'rating': 5,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_rating_field_is_required(self):
        """ Test review rating field is required """
        form = ReviewForm({
            'content': 'This is a test review',
            'rating': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Test fields are explicit in form metaclass """
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ('content', 'rating'))
