from django.db import models


# Para as dias classes se comportarem da mesma forma / atribuir data de atualizção e criação
class TimestambleMixin(models.Model):
    # Vai pegar data hora do momento
    created_at = models.DateTimeField(auto_now_add=True)
    # toda vez que for atualizado
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Product(TimestambleMixin):
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    stock_max = models.IntegerField()
    price_sale = models.DecimalField(decimal_places=2, max_digits=6)
    price_purchase = models.DecimalField(decimal_places=2, max_digits=6)


class StockEntry(TimestambleMixin):
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

