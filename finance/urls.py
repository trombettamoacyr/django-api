"""finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import home, list_transactions, create_transaction, update_transaction, delete_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('transactions', list_transactions, name='url_list_transactions'),
    path('transactions/new', create_transaction),
    path('transactions/update/<int:pk>', update_transaction, name='url_update_transaction'),
    path('transactions/delete/<int:pk>', delete_transaction, name='url_delete_transaction'),
]
