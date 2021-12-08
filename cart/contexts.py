# Adapted from Boutique Ado walkthrough project by Code Institute

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import Discount


def cart_contents(request):
    discount_id = request.session.get('discount_id', int())
    cart_items = []
    cart_total = 0
    total = 0
    product_count = 0
    discount_amount = 0
    discount_savings = 0
    cart = request.session.get('cart', {})

    # Check discount code against Discount model
    try:
        discount = Discount.objects.get(id=discount_id)
    except Discount.DoesNotExist:
        discount = None

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, id=item_id)
        cart_total += quantity * product.price

        if discount is not None:
            discount_amount = discount.amount
            discount_savings = cart_total*(discount_amount/Decimal('100'))
            total = cart_total - discount_savings
        else:
            total = cart_total

        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount': discount,
        'discount_amount': discount_amount,
        'discount_savings': discount_savings,
        'cart_total': cart_total,
    }

    return context
