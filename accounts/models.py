from tabnanny import verbose
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Transaction(models.Model):
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    notes = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'transactions'

    def __str__(self):
        return self.description