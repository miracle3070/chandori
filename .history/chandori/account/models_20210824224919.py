from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    job = models.CharField(max_length=20)
    income = models.IntegerField(null=True)
    signup_date = models.DateTimeField(null=True)

class BankAccount(AbstractBaseUser):
    custom_id = models.ForeignKey("CustomUser", related_name="customuser", on_delete=models.CASCADE, db_column="custom_id")
    account_num = models.IntegerField(null=True)
    bank = models.CharField(max_length=20)
    balance = models.IntegerField(null=True)
    # USERNAME_FIELD = 'bank'
    # REQUIRED_FIELDS = ['account_num']