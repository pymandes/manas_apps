from django.db import models
from django.utils.timezone import now

# Create your models here.
class ExpenseType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=256)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=256)
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
