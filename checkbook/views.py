from django.http import HttpResponse
from django.template import loader
from django import forms
from django.shortcuts import render

from .models import Account, Category, Transaction

def index(request):
    account_list = Account.objects.all()
    template = loader.get_template('checkbook/index.html')
    context = {
        'account_list': account_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, account_name_id):
    account = Account.objects.get(pk=account_name_id)
    transactions = account.transactions()
    available = account.available_balance()
    actual = account.actual_balance()
    transaction_list = []
    for v in reversed(transactions): # This lists the transactions backwards, but maybe this a is a definiable use preference
        if v.not_clear == True:
            transaction_list.append(v)
        else:
            continue
    for v in reversed(transactions):
        if v.not_clear == False:
            transaction_list.append(v)
    template = loader.get_template('checkbook/detail.html')
    context = {
        'transaction_list': transaction_list,
        'account_name': account,
        'available': available,
        'actual': actual,
    }
    return HttpResponse(template.render(context, request))

def create_account(request):
    template = loader.get_template('checkbook/create_account.html')
    context = {}
    return HttpResponse(template.render(context, request))
 
def account_confirmation(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('balance'):
            name = request.POST.get('name')
            balance = request.POST.get('balance')
            new_account=Account(account_name=name, start_balance=balance)
            new_account.save()
            context = {
                "message": new_account.account_name, 
                "start_balance": new_account.start_balance
                }
            return render(request, 'checkbook/account_confirmation.html', context)
    else:
            return render(request, 'checkbook/account_confirmation.html', context)

def create_transaction(request, account_name_id):
    account = Account.objects.get(pk=account_name_id)
    categories = Category.objects.all().order_by('category_name')
    template = loader.get_template('checkbook/create_transaction.html')
    context = {
        "account": account,
        "categories": categories,
        }
    return HttpResponse(template.render(context, request))

def transaction_confirmation(request, account_name_id):
    account = Account.objects.get(pk=account_name_id)
    if request.method == 'POST':
        if request.POST.get('type') and request.POST.get('amount') and request.POST.get('memo') and request.POST.get('category'):
            transtype = request.POST.get('type')
            amount = request.POST.get('amount')
            not_clear = request.POST.get('not_clear')
            if not_clear == None:
                not_clear = False
            else:
                not_clear = True
            memo = request.POST.get('memo')
            category = request.POST.get('category')
            category = Category.objects.get(pk=int(category))
            new_transaction = Transaction(account_name_id=account_name_id, amount=amount, transaction_type=transtype, memo=memo, category=category, not_clear=not_clear)
            new_transaction.save()
            context = {
                    "transaction": new_transaction,
                    "account": account,
                }
            return render(request, 'checkbook/transaction_confirmation.html', context)
    else:
            return render(request, 'checkbook/transaction_confirmation.html', context)