from django.forms import ModelForm
from .models import Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['id', 'description', 'value', 'category', 'notes']