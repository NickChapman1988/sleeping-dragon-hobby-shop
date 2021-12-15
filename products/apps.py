""" Products App """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ Config for Products app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        """ Ready function for Products app """
        import products.signals
