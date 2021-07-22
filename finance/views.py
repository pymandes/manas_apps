from finance.models import Transactions
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from finance.forms import ExpenseForm, ExpenseTypeForm, ExpenseCategoryForm
from django.db.models import Q

# Create your views here.
class ExpenseFormView(View):
    template_name = 'expense/add_expense.html'

    def get(self, request):

        return HttpResponse(self.template_name)


class SearchTransactionsView(ListView):
    model = Transactions
    template_name = 'transactions/search_transactions.html'
    print("here")

    # def get_queryset(self):
    #     transactions = []
    #     name = self.request.GET.get('tname', None)
    #     value = self.request.GET.get('tvalue', None)
    #     to = self.request.GET.get('tto', None)
    #     tfrom = self.request.GET.get('tfrom', None)

    #     if name:
    #         transactions = Transactions.objects.filter(Q(name__icontains=name))

    #     else:
    #         transactions = Transactions

    #     return transactions

