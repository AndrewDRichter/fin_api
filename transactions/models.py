from django.db import models
from app.settings import CURRENCY_OPTIONS
from accounts.models import UserAccount


TRANSACTION_TYPE_CHOICES = (
    ('INCOME', 'Entrada'),
    ('EXPENSE', 'Saída'),
)


TRANSACTION_STATUS_CHOICES = (
    ('PAID', 'Paga'),
    ('PENDING', 'Pendente'),
    ('CANCELLED', 'Cancelada'),
)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    description = models.TextField(blank=True, null=True)
    type = models.CharField(
        max_length=100,
        choices=TRANSACTION_TYPE_CHOICES
    )
    category = models.ForeignKey(
        TransactionCategory,
        on_delete=models.PROTECT
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=18
    )
    currency = models.CharField(
        max_length=100,
        choices=CURRENCY_OPTIONS
    )
    transaction_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT
    )
    account = models.ForeignKey(
        UserAccount,
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    status = models.CharField(
        max_length=100,
        choices=TRANSACTION_STATUS_CHOICES
    )
    is_recurring = models.BooleanField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
