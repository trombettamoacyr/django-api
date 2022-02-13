from django.shortcuts import render
from .models import Transaction
from .form import TransactionForm

def home(request):
    return render(request, 'accounts/home.html')

def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions.html', {'transactions': transactions})

def create_transaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return list_transactions(request)
    return render(request, 'transactions/form.html', {'form': form})