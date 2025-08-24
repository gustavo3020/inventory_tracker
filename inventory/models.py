from django.db import models


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.product_name


class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
