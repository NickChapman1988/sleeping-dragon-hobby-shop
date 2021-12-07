"""
Products app signal config module
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review


@receiver(post_save, sender=Review)
def update_rating_on_review(sender, instance, **kwargs):
    """ Update product rating when reviewed """
    instance.product.calculate_rating()


@receiver(post_delete, sender=Review)
def update_rating_on_delete(sender, instance, **kwargs):
    """ Update product rating when review deleted """
    if instance.product:
        instance.product.calculate_rating()
