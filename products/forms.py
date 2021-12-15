""" Forms for Products app """
# pylint: disable=no-member
# pylint: disable=unused-variable
# pylint: disable=too-few-public-methods
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """ A form for products """

    class Meta:
        """ Metadata for ProductForm """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """ init method for ProductForm """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CategoryForm(forms.ModelForm):
    """ A form for categories """

    class Meta:
        """ Metadata for CategoryForm """
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """ init method for CategoryForm """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """ A form for reviews """

    class Meta:
        """ Metadata for ReviewForm """
        model = Review
        fields = ('content', 'rating')
        labels = {
            'content': 'Review',
            'rating': 'Rating',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['autofocus'] = True
        self.fields['rating'].widget.attrs['min'] = 1
        self.fields['rating'].widget.attrs['max'] = 5
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 review-input'
