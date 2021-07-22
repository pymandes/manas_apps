from django.urls import include, path
from django.views.generic import TemplateView
from finance.views import SearchTransactionsView

app_name='finance'
urlpatterns = [
    path("add_expense", TemplateView.as_view(template_name="expense/add_expense.html"), name="add_expense"),
    path("search_transactions", TemplateView.as_view(template_name="transactions/search_transactions.html"), name="search_transactions"),
    path("transaction_results/", SearchTransactionsView.as_view(), name="transaction_results"),
]