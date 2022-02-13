from django.shortcuts import render, redirect
from .models import Transaction
from .form import TransactionForm

def home(request):
    return render(request, 'accounts/home.html')

def list_transactions(request):
    print('list')
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions.html', {'transactions': transactions})

def create_transaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_list_transactions')
    return render(request, 'transactions/form.html', {'form': form})

def update_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        return redirect('url_list_transactions')
    return render(request, 'transactions/form.html', {'form': form, 'id': transaction.id})

def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return list_transactions(request)

