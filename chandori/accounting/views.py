from django.shortcuts import render, redirect
from .models import *
import re

def home(request):
    return render(request, "base.html")

# 정규표현식
p = re.compile("money[0-9]+")


# 가계부 입력 view
def field(request):
    if request.method == "POST":
        # 전달받은 데이터 중에서 money* 항목 이름만 얻어옴.
        recv_data = request.POST.keys()
        temp1 = " ".join(recv_data)
        moneys = p.findall(temp1)
        print(moneys)

        # 금액이 비어있는 거래내역은 삭제
        for m in moneys[:]:
            if request.POST[m] == "":
                moneys.remove(m)

        numbers = []
        # money* 에서 *(숫자)만 추출
        for i in range(len(moneys)):
            num = moneys[i][5:]
            numbers.append(num)

        print(numbers)

        for n in numbers:
            print(request.POST.keys())
            user_id = request.POST["user"]
            user = CustomUser.objects.get(pk=user_id)
            bank_account = request.POST["bank_account" + n]
            
            if ("is-income" + n) in request.POST:
                type = "수입"
            else:
                type = "지출"
            
            category = request.POST["category" + n]
            money = request.POST["money" + n]
            date = request.POST["date"]
            memo = request.POST["memo" + n]

            transaction_info = TestInfoModel.objects.create(
                user = user,
                bank_account = bank_account,
                type = type,
                category = category,
                money = money,
                date = date,
                memo = memo
            )

            transaction_info.save()
            return redirect("accounting:home")


    return render(request, "account-field.html")