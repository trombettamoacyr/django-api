from django.contrib import admin
from accounts.models import Category
from accounts.models import Transaction

admin.site.register(Category)
admin.site.register(Transaction)