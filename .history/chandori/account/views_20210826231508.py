from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone
from .models import *
from .models import BankAccount
from .forms import CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def edit(request):
    user_change_form = CustomUserChangeForm(request.POST, instance = request.user)
    user_change_form.nickname = request.POST.get('nickname')
    user_change_form.age = request.POST.get('age')
    user_change_form.job = request.POST.get('job')
    user_change_form.income = request.POST.get('income')
    bankforms = BankAccount.objects.filter(name = user_change_form.nickname)
    if request.method == 'GET':
        return render(request, 'edit.html', {'bankforms':bankforms})
    elif request.method == 'POST':
        user_change_form.save()
        messages.success(request, '회원정보가 수정되었습니다.')
        return render(request, 'edit.html', {'bankforms':bankforms})
    return render(request, 'edit.html', {'bankforms':bankforms})
       
def edit_bank(request):
    add_Account = BankAccount()
    user_change_form = CustomUserChangeForm(request.POST, instance = request.user)
    add_Account.name = request.POST.get('name')
    user_change_form.nickname = request.POST.get('name')
    add_Account.account_num = request.POST.get('account_num')
    add_Account.bank = request.POST.get('bank')
    add_Account.balance = request.POST.get('balance')
    
    bankforms = BankAccount.objects.filter(name = user_change_form.nickname)
    if request.method == 'GET':
        return render(request, 'add_Account.html', {'bankforms':bankforms})
    elif request.method == 'POST':
        add_Account.save()
        return render(request, 'add_Account.html', {'bankforms':bankforms})
    return render(request, 'add_Account.html', {'bankforms':bankforms})
    
def bank_delete(request, BankAccount_id):
    get_object_or_404(BankAccount, pk=BankAccount_id).delete()
    return redirect('/add_Account/')

def login_view(request):
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "" or password == "":
            error_msg = "아이디 또는 비밀번호를 입력해주세요."            
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("accounting:home")
            else:
                error_msg = "아이디 또는 비밀번호가 틀렸습니다."
    return render(request, "login.html", {"error_msg" : error_msg})

def logout_view(request):
    logout(request)
    return redirect("accounting:home")

def signup_view(request):
    error_msg = ""
    if request.method == "POST":
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            username = request.POST["username"]
            nickname = request.POST["nickname"]
            age = int(request.POST['age'])
            job = request.POST['job']
            income = int(request.POST['income'])
            signup_date = timezone.now()

            user = CustomUser.objects.create_user(
                username = username,
                password = password1,
                nickname = nickname,
                age = age,
                job = job,
                income = income,
                signup_date = signup_date,
            )

            return redirect("account:login")
        else:
            error_msg = "비밀번호가 일치하지 않습니다."

    return render(request, "signup.html", {"error_msg" : error_msg})

   
