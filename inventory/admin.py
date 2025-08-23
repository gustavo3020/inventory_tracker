from django.contrib import admin
from .models import Location, Product, StockTransaction

admin.site.register(Location)
admin.site.register(Product)
admin.site.register(StockTransaction)
