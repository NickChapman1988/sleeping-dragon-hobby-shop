from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'stock',
        'brand',
        'rating',
        'image',
    )

    ordering = ('sku'),


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """ Admin configuration for Review model """
    list_display = (
        'user',
        'product',
    )
    ordering = ['user', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
