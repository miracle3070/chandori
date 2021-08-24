from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone
from .models import *
from .forms import CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def edit(request):
    if request.method == 'GET':
        return render(request, 'edit.html')
    elif request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)
        user_change_form.nickname = request.POST['nickname']
        user_change_form.age = request.POST['age']
        user_change_form.job = request.POST['job']
        user_change_form.income = request.POST['income']
        user_change_form.save()
        messages.success(request, '회원정보가 수정되었습니다.')
        return redirect('account:edit', request.user)
        # if user_change_form.is_valid():
            
    # else:
    #     user_change_form = CustomUserChangeForm(instance = request.user)

    #     return render(request, 'edit.html', {'user_change_form':user_change_form})


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

   
