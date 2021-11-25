# Adapted from Boutique Ado walkthrough project by Code Institute

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on order line item create or update
    """
    print('saved message, signals work, look at me!')
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on line item delete
    """
    print('you deleted me, you fool!')
    instance.order.update_total()
