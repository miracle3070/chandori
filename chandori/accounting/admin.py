from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BankAccount)
admin.site.register(TransactionInfo)
admin.site.register(TestInfoModel)