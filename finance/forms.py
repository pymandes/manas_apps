from django.forms import ModelForm, fields
from finance.models import Expense, ExpenseCategory, ExpenseType, Transactions
from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        exclude = ['created', 'updated']


class ExpenseTypeForm(ModelForm):
    class Meta:
        model = ExpenseType
        exclude = ['created', 'updated']


class ExpenseCategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        exclude = ['created', 'updated']
