from django.contrib import admin
from finance.models import ExpenseCategory, ExpenseType, Expense, TransactionCategory, TransactionType, Transactions, Actors

# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(ExpenseType)
admin.site.register(Expense)
admin.site.register(Transactions)
admin.site.register(TransactionCategory)
admin.site.register(TransactionType)
admin.site.register(Actors)