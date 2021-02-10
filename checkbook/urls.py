from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account-<int:account_name_id>/', views.detail, name="account_detail"),
    path('create_account/', views.create_account, name="create_account"),
    path('account_confirmation/', views.account_confirmation, name="account_confirmation"),
    path('account-<int:account_name_id>/add_transaction/', views.create_transaction, name="add_transaction"),
    path('account-<int:account_name_id>/add_transaction/transaction_confirmation/', views.transaction_confirmation, name="transaction_confirmation"),
]