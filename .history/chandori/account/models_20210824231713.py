from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    job = models.CharField(max_length=20)
    income = models.IntegerField(null=True)
    signup_date = models.DateTimeField(null=True)

