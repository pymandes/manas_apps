from django.contrib import admin
from finance.models import ExpenseCategory, ExpenseType, Expense

# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(ExpenseType)
admin.site.register(Expense)