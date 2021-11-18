from django.contrib import admin
from .models import Product, Category

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

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
