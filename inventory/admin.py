from django.contrib import admin
from .models import Location, Product, StockTransaction


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'address')
    search_fields = ('location_name', 'address')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description')
    search_fields = ('product_name', 'description')

class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'transaction_type')
    search_fields = ('product', 'location', 'transaction_type')


admin.site.register(Location, LocationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(StockTransaction, StockTransactionAdmin)
