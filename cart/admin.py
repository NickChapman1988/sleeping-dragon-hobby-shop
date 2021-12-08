from django.contrib import admin
from .models import Discount


class DiscountAdmin(admin.ModelAdmin):
    """ Admin for the Discount model """
    list_display = ['code', 'valid_from', 'valid_to', 'amount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']


admin.site.register(Discount, DiscountAdmin)
