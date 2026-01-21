from django.shortcuts import render
from .models import Expense, Income


def profit_loss(request):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()

    total_expense = sum(e.amount for e in expenses)
    total_income = sum(i.amount for i in incomes)

    profit = total_income - total_expense

    return render(request, 'finance/profit.html', {
        'expenses': expenses,
        'incomes': incomes,
        'expense': total_expense,
        'income': total_income,
        'profit': profit
    })

