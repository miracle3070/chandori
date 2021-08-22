from django.urls import path
import account.views

app_name = 'account'

urlpatterns = [
    path('', account.views.edit, name="edit"),
]