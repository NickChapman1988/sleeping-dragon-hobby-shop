""" Cart app views """
# pylint: disable=no-member
# pylint: disable=broad-except
import datetime

from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from django.views.decorators.http import require_POST

from products.models import Product
from .models import Discount


def view_cart(request):
    """ A view that renders the cart contents page """
    on_cart_page = True
    context = {
        'on_cart_page': on_cart_page,
    }

    return render(request, 'cart/cart.html', context)


@require_POST
def discount_apply(request):
    """ Apply discount code """
    now = datetime.datetime.now()
    code = request.POST.get('discount-code')

    if not code:
        messages.error(request, "You didn't enter a coupon code!")
        return redirect(reverse('view_cart'))

    try:
        discount = Discount.objects.get(code=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
        request.session['discount_id'] = discount.id
        messages.success(request, f'Discount code { code } applied')
    except Discount.DoesNotExist:
        request.session['discount_id'] = None
        messages.error(request, f'Discount code {code} is not valid')
        return redirect('view_cart')
    else:
        return redirect('view_cart')


def cancel_discount(request):
    """ Cancel applied discount """
    request.session['discount_id'] = None

    return redirect('view_cart')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, id=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # Check cart quantity is less than product stock
        if cart[item_id] < product.stock:
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        # If cart quantity already equals product stock,
        # display warning and prevent addition of stock
        elif cart[item_id] >= product.stock:
            messages.warning(
                request, f'Sorry, you cannot add that many {product.name} to your cart. \
                We have {product.stock} in stock, \
                and you already have {cart[item_id]} in your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, id=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        # Check cart quantity is less than product stock
        if cart[item_id] <= product.stock:
            # Check updated quantity is less than stock
            if quantity <= product.stock:
                cart[item_id] = quantity
                messages.success(
                    request, f'Updated {product.name} quantity to {cart[item_id]}')
            else:
                messages.warning(
                request, f'Sorry, you cannot add that many {product.name} to your cart. \
                We have {product.stock} in stock, \
                and you already have {cart[item_id]} in your cart')
        # If cart quantity already equals product stock,
        # display warning and prevent addition of stock
        elif cart[item_id] > product.stock:
            if quantity <= product.stock:
                cart[item_id] = product.stock
                messages.success(
                    request, f'Updated {product.name} quantity to {cart[item_id]}')
            else:
                messages.warning(
                    request, f'Sorry, you cannot add any more {product.name} to your cart. \
                    We have {product.stock} in stock, \
                    and you already have {cart[item_id]} in your cart')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        product = get_object_or_404(Product, id=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as error:
        messages.error(request, f'Error removing item: {error}')
        return HttpResponse(status=500)
