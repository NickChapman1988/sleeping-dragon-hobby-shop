# Adapted from Boutique Ado walkthrough project by Code Institute

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from checkout.models import Order
from .models import Product, Category, Review
from .forms import ProductForm, CategoryForm, ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    categories = None
    brand = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # filter by product brand
        if 'brand' in request.GET:
            brand = request.GET['brand']
            products = Product.objects.filter(brand=brand)
            brand = Product.objects.filter(brand__in=products)

        # filter by product category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # filter by search query
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brand': brand,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    # Get individual product
    product = get_object_or_404(Product, id=product_id)

    # Get latest product reviews
    product_reviews = Review.objects.filter(
        product=product).order_by("date")[:10]
    user_review = None

    # If user is authenticated, get user review if available
    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            product=product, user=request.user).first()

    context = {
        'product': product,
        'product_reviews': product_reviews,
        'user_review': user_review,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def product_management(request):
    """ A view for admin users to manage products
    and categories from the storefront """

    # Prevent all except superusers accessing product management
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    products = Product.objects.all()
    categories = Category.objects.all()
    latest_orders = Order.objects.all()[:5]

    # Sort categories alphabetically
    categories = categories.order_by('name')

    context = {
        'products': products,
        'categories': categories,
        'latest_orders': latest_orders,
    }

    return render(request, 'products/product_management.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    # Prevent all except superusers accessing product management
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please \
                ensure the form is valid'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    # Prevent all except superusers accessing product management
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
            Please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # Prevent all except superusers accessing product management
    """ Delete a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    if reviews:
        reviews.delete()
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))


@login_required
def add_category(request):
    """ Add a category to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Successfully added category')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add category. \
                Please ensure the form is valid')
    else:
        form = CategoryForm()

    template = 'products/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    """ Edit a category in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully updated {category.display_name}')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to update category. \
                Please ensure the form is valid')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.display_name}')

    template = 'products/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ Delete a category in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, 'Category deleted')
    return redirect(reverse('product_management'))


@login_required
def review_product(request, product_id):
    """ Review a product """

    # Get product
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':

        # Get existing user review
        product_review = Review.objects.filter(
            product=product, user=request.user)

        # If user review exists
        if product_review:
            new_review = False
            review_form = ReviewForm(request.POST, instance=product_review)
        else:
            # Create blank review form
            new_review = True
            review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            # Create and save new review
            if new_review:
                # Create review
                review = review_form.save(commit=False)
                # Add review to product
                review.product = product
                # Add user to review
                review.user = request.user
                # Save review
                review.save()
                messages.success(
                    request, f'Review successfully added for {product.name}')
            else:
                # Update review
                review_form.save()
                messages.success(
                    request, f'Review successfully updated for {product.name}')
                return redirect(reverse('product_detail', args=[product.id]))
        else:
            # If form not valid
            if new_review:
                messages.error(
                    request, 'Failed to add review. \
                    Please ensure the form is valid')
            else:
                messages.error(
                    request, 'Failed to update review. \
                    Please ensure the form is valid')
    else:
        product_review = Review.objects.filter(
            product=product, user=request.user)

        if product_review:
            review_form = ReviewForm(instance=product_review)
        else:
            review_form = ReviewForm

    template = 'products/review_product.html'
    context = {
        'product': product,
        'product_review': product_review,
        'review_form': review_form,
    }

    return render(request, template, context)
