from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    job = models.CharField(max_length=20)
    income = models.IntegerField(null=True)
    signup_date = models.DateTimeField(null=True)

class BankAccount(AbstractUser):
    custom_id = models.ForeignKey("CustomUser", related_name="CustomUser", on_delete=models.SET_NULL, db_column="custom_id")
    account_num = models.IntegerField(null=True)
    bank = models.CharField(max_length=20)
    balance = models.IntegerField(null=True)
    