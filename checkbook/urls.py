from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:account_name_id>/', views.detail, name="account_id"),
    path('create_account/', views.create_account, name="create_account"),
    path('account_confirmation/', views.account_confirmation, name="account_confirmation"),
    path('<int:account_name_id>/create_transaction/', views.create_transaction, name="create_transaction"),
    path('<int:account_name_id>/create_transaction/transaction_confirmation/', views.transaction_confirmation, name="transaction_confirmation"),
]