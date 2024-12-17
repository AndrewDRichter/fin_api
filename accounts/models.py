from django.db import models
from django.contrib.auth.models import User
from app.settings import CURRENCY_OPTIONS


STATUS_CHOICES = (
    (False, 'Inactive'),
    (True, 'Active'),
)


class AccountType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    balance = models.DecimalField(decimal_places=2, max_digits=18)
    currency = models.CharField(max_length=100, choices=CURRENCY_OPTIONS)
    institution = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(choices=STATUS_CHOICES)
    # ISO8601 for datetime format standarts
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.currency}'


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user} - {self.account}'
