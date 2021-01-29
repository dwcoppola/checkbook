from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class Account(models.Model):
    account_name = models.CharField(max_length=50)
    start_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def available_balance(self):
        t_all = Transaction.objects.all()
        amounts = []
        for v in t_all:
            if v.account_name_id != self.id:
                continue
            if v.transaction_type == "withdrawal":
                amounts.append(v.amount * -1)
            else:
                if v.not_clear == False:
                    amounts.append(v.amount)
                else:
                    continue
        available = self.start_balance
        for v in amounts:
            available += v
        return available
    
    def actual_balance(self):
        t_all = Transaction.objects.all()
        amounts = []
        for v in t_all:
            if v.account_name_id != self.id:
                continue
            elif v.not_clear == False:
                if v.transaction_type == "withdrawal":
                    amounts.append(v.amount * -1)
                else:
                    amounts.append(v.amount)
            else:
                continue
        actual = self.start_balance
        for v in amounts:
            actual += v
        return actual
    
    def transactions(self):
        t_all = Transaction.objects.all()
        transactions = []
        for v in t_all:
            if v.account_name_id == self.id:
                transactions.append(v)
        return transactions       

    def __str__(self):
        return f"{self.account_name}"

class Transaction(models.Model):
    account_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=[('deposit','deposit'), ('withdrawal','withdrawal')])
    amount = models.DecimalField(max_digits=10, decimal_places=2, )
    memo = models.CharField(max_length=50, blank=True, default=" -- ")
    category = models.ForeignKey(Category, default=13, on_delete=models.CASCADE)
    not_clear = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.transaction_type == "withdrawal":
            return f"-${self.amount} from {self.account_name} ({str(self.time)[:19]})"
        elif self.transaction_type == "deposit":
            return f"${self.amount} into {self.account_name} ({str(self.time)[:19]})"