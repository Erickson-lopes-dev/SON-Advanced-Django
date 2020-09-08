from django.core.mail import send_mail
from django.dispatch.dispatcher import Signal
from django.template.loader import render_to_string

from django_avancado.settings import MAIL_REPLY

product_stock_changed = Signal


class Mailple:
    def sendMail(self, from_email, to, subject, template, context=None):
        if context is None:
            context = {}
        html = render_to_string(template, {})
        send_mail(
            from_email=from_email,
            recipient_list=(to,),
            subject=subject,
            message=subject,
            html_message=html
        )


class StockGreaterMax(Mailple):
    def __init__(self, product):
        self.product = product

    def send(self, to):
        super().sendMail(
            from_email=MAIL_REPLY,
            to=to,
            subject=f'Estoque de Produto {self.product.name} esta acima do maximo',
            template='emails/stock-greater-max.html',
            context={'product': self.product}
        )
