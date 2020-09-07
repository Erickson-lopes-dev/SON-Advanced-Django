from django.db import models


class Product(models.Model):
    name = models.Charfield(mex_lenght=255)
    stock = models.IntegerField(default=0)
    stock_max = models.IntegerField()
    price_sale = models.DecimalField(decimal_places=2, max_digits=6)
    price_purchase = models.DecimalField(decimal_places=2, max_digits=6)
