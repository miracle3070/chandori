from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    id = models.BigAutoField(help_text="CustomUser ID", primary_key=True)
    nickname = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    job = models.CharField(max_length=20)
    income = models.IntegerField(null=True)
    signup_date = models.DateTimeField(null=True)


class BankAccount(models.Model):
    id = models.BigAutoField(help_text="BankAccount ID", primary_key=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True, related_name="bankAccount", on_delete=models.CASCADE, db_column="user")
    name = models.CharField(max_length=30)
    account_num = models.CharField(max_length=30)
    bank = models.CharField(max_length=20)
    balance = models.IntegerField(null=True)
