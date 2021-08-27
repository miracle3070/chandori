from django.shortcuts import render, redirect
from django.utils.dateformat import DateFormat
from .models import *
from datetime import datetime
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
        #print(moneys)

        # 금액이 비어있는 거래내역은 삭제
        for m in moneys[:]:
            if request.POST[m] == "":
                moneys.remove(m)

        numbers = []
        # money* 에서 *(숫자)만 추출
        for i in range(len(moneys)):
            num = moneys[i][5:]
            numbers.append(num)

        #print(numbers)

        # 기존에 해당 날짜에 존재했던 가계부 데이터 삭제
        exist_info = TestInfoModel.objects.filter(
            user=request.user,
            date = request.POST["date"]
            )        
        for e in exist_info:
            e.delete()

        # 입력한 가계부 데이터 저장
        for n in numbers:
            user_id = request.POST["user"]
            user = CustomUser.objects.get(pk=user_id)
            bank_account = request.POST["bank_account" + n]
            
            if ("is-income" + n) in request.POST:
                type1 = "수입"
            else:
                type1 = "지출"
            
            category = request.POST["category" + n]
            money = request.POST["money" + n]
            date = request.POST["date"]
            memo = request.POST["memo" + n]

            transaction_info = TestInfoModel.objects.create(
                user = user,
                bank_account = bank_account,
                type = type1,
                category = category,
                money = money,
                date = date,
                memo = memo
            )

            transaction_info.save()
        return redirect("accounting:setField", date)

    # method가 GET 방식일 경우
    today = DateFormat(datetime.now()).format("Y-m-d")
    trans = list(TestInfoModel.objects.filter(user=request.user.pk, date=today))
    return render(request, "account-field.html", {"trans" : trans, "dateString": 0})


def setField(request, date):
    print("안녕하세요!")
    print(date)
    trans = list(TestInfoModel.objects.filter(user=request.user.pk, date=date))
    return render(request, "account-field.html", {"trans" : trans, "dateString" : date})