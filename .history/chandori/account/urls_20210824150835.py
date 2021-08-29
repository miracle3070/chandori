from django.urls import path
import account.views

app_name = 'account'

urlpatterns = [
    path('', account.views.edit, name="edit"),
    path('login/', account.views.login_view, name="login"),
    path('logout/', account.views.logout_view, name="logout"),
    path('signup/', account.views.signup_view, name="signup"),
    
]