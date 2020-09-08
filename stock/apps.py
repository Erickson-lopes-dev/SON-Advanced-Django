from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'stock'

    def ready(self):
        from stock import signals