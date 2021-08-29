from django.urls import path
import account.views

app_name = 'account'

urlpatterns = [
    path('', account.views.edit, name="edit"),
    path('add_Account/', account.views.edit_bank, name="edit_bank"),
    path('delete/<int:BankAccount_id>/', account.views.bank_delete, name="delete"),
    path('login/', account.views.login_view, name="login"),
    path('logout/', account.views.logout_view, name="logout"),
    path('signup/', account.views.signup_view, name="signup"),
    path('detail/<int:BankAcount_id>/', account.views.bank_detail, name="detail"),
]