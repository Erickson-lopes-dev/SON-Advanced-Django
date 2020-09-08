from django.db.models.signals import post_save

from stock.models import StockEntry


# receptor
def increment_stock(sender, instance, **kwargs):
    product = instance.product
    product.stock = product.stock + instance.amount
    product.save()


def test_save(sender, instance, created, **kwargs):
    print(created+"*******************")


post_save.connect(increment_stock, sender=StockEntry)
post_save.connect(test_save, sender=StockEntry)
