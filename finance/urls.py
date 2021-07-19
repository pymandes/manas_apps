from django.urls import include, path
from django.views.generic import TemplateView

app_name='finance'
urlpatterns = [
    path("add_expense", TemplateView.as_view(template_name="expense/add_expense.html"), name="add_expense"),
]