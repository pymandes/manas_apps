from config.settings.base import STATICFILES_FINDERS
from django.db import models
from django.utils.timezone import now

# Create your models here.
class ExpenseType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=256, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=256, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(ExpenseType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    estimated = models.FloatField()
    actual = models.FloatField()
    date = models.DateTimeField(default=now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name + '-' + self.type.name + '-' + self.category.name + '-' + str(self.actual)


class TransactionType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=256, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Actors(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=256, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Transactions(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(TransactionType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(TransactionCategory, on_delete=models.SET_NULL, null=True)
    value = models.FloatField()
    sender = models.ForeignKey(Actors, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_sender")
    receiver = models.ForeignKey(Actors, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_receiver")
    date = models.DateTimeField(default=now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name + '-' + self.type.name + '-' + self.category.name + '-' + str(self.value)
