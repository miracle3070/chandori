from django.db import models
from account.models import *

# 계좌정보 모델 (임시용)
class BankAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank = models.CharField(max_length=20)
    account_num = models.CharField(max_length=20)
    balance = models.IntegerField()

# 거래내역 모델
class TransactionInfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    money = models.IntegerField()
    date = models.DateField()
    memo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + " - " + self.user.username + " - " + str(self.date)

# 시험용 거래내역 모델
class TestInfoModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank_account = models.CharField(max_length=20) # 이 부분이 다름
    type = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    money = models.IntegerField()
    date = models.DateField()
    memo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + " - " + self.user.username + " - " + str(self.date)


