from django.shortcuts import render, redirect
from django.utils.dateformat import DateFormat
from account.models import BankAccount
from datetime import datetime
import calendar
import re
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.contrib.auth.decorators import login_required
from account.models import *
from .models import *
# Create your views here.

def home(request):
    #로그인한 유저의 통계
    today = DateFormat(datetime.now()).format('m')#현재의 월
    logined_consum = TransactionInfo.objects.filter(user_id = request.user.id, date__month=today)#로그인한 유저의 이번달 모든 소비내역
    logined_food = 0
    logined_transport = 0
    logined_snacks = 0
    logined_mart = 0
    logined_shopping = 0
    logined_entertainment = 0
    logined_medical = 0
    logined_utility = 0
    logined_etc = 0
    #각 소비내역 합산
    for result in logined_consum:
        if result.category == "식비":
            logined_food += result.money
        elif result.category == "교통":
            logined_transport += result.money
        elif result.category == "카페.간식":
            logined_snacks += result.money
        elif result.category == "편의점.마트":
            logined_mart += result.money
        elif result.category == "쇼핑":
            logined_shopping += result.money
        elif result.category == "술.유흥":
            logined_entertainment += result.money
        elif result.category == "의료비":
            logined_medical += result.money
        elif result.category == "공과금":
            logined_utility += result.money
        elif result.category == "기타":
            logined_etc += result.money

    #합산한 소비내역으로 딕셔너리를 만듬
    logined_consum_list = {"식비":logined_food, "교통":logined_transport, "카페.간식":logined_snacks, "편의점.마트":logined_mart, "쇼핑":logined_shopping, "술.유흥":logined_entertainment, "의료비":logined_medical, "공과금":logined_utility, "기타":logined_etc}
    sorted_logined_consum_list = dict(sorted(logined_consum_list.items(), key=lambda x:x[1], reverse=True))#가장 많이 쓴 항목이 그래프에서 먼저 나올 수 있도록 내림차순으로 정렬
    logined_total = sum(logined_consum_list.values()) #모든항목 소비내역 합

    #여기서부터 모든 유저의 통계 --> 로그인한 유저가 상위 n%임을 출력하기 위함
    #각 유저들의 각 항목에 대한 토탈값 리스트
    sum_total_list = []
    food_total_list = []
    transport_total_list = []
    snacks_total_list = []
    mart_total_list = []
    shopping_total_list = []
    entertainment_total_list = []
    medical_total_list = []
    utility_total_list = []
    etc_total_list = []

    user_list = CustomUser.objects.filter()
    for id in user_list:
        TransactionInfos = TransactionInfo.objects.filter(user_id = id, date__month=today)#n번 Id 유저의 이번달 모든 소비내역
        #n번 Id 유저의 카테고리별 소비금액 변수
        total = 0 #n번 Id 유저의 총 소비금액 변수
        food = 0 
        transport = 0
        snacks = 0
        mart = 0
        shopping = 0
        entertainment = 0
        medical = 0
        utility = 0
        etc = 0

        #n번 Id 유저의 카테고리별 소비내역 합산
        for result in TransactionInfos:
            if result.category == "식비":
                food += result.money
                total += result.money#n번 Id 유저의 총 소비 금액을 구하기 위함
            elif result.category == "교통":
                transport += result.money
                total += result.money
            elif result.category == "카페.간식":
                snacks += result.money
                total += result.money
            elif result.category == "편의점.마트":
                mart += result.money
                total += result.money
            elif result.category == "쇼핑":
                shopping += result.money
                total += result.money
            elif result.category == "술.유흥":
                entertainment += result.money
                total += result.money
            elif result.category == "의료비":
                medical += result.money
                total += result.money
            elif result.category == "공과금":
                utility += result.money
                total += result.money
            elif result.category == "기타":
                etc += result.money
                total += result.money

        #n번 Id 유저의 카테고리별 소비내역을 리스트에 추가
        sum_total_list.append(total)
        food_total_list.append(food)
        transport_total_list.append(transport)
        snacks_total_list.append(snacks)
        mart_total_list.append(mart)
        shopping_total_list.append(shopping)
        entertainment_total_list.append(entertainment)
        medical_total_list.append(medical)
        utility_total_list.append(utility)
        etc_total_list.append(etc)
        # consum_list = {"식비":food, "교통비":transport, "카페.간식":snacks, "편의점.마트":mart, "쇼핑":shopping, "술.유흥":entertainment, "의료비":medical, "공과금":utility, "기타":etc}
    
    #유저들의 카테고리별 소비내역을 내림차순으로 정렬
    sum_total_list.sort()# 모든 유저의 이번달 전체소비내역이 담긴 내림차순 리스트
    sum_total_list_len = len(sum_total_list)# 리스트의 길이
    logined_total_index = sum_total_list.index(logined_total)+1 #로그인한 유저의 이번달 전체소비내역 순위(인덱스 값으로 나오니 +1)
    total_p = round(logined_total_index/sum_total_list_len*100, 2)
    
    food_total_list.sort()
    food_total_list_len = len(food_total_list)
    logined_food_index = food_total_list.index(logined_food)+1
    food_p = round(logined_food_index/food_total_list_len*100,2)

    transport_total_list.sort()
    transport_total_list_len = len(transport_total_list)
    logined_transport_index = transport_total_list.index(logined_transport)+1
    transport_p = round(logined_transport_index/transport_total_list_len*100,2)

    snacks_total_list.sort()
    snacks_total_list_len = len(snacks_total_list)
    logined_snacks_index = snacks_total_list.index(logined_snacks)+1
    snacks_p = round(logined_snacks_index/snacks_total_list_len*100,2)

    mart_total_list.sort()
    mart_total_list_len = len(mart_total_list)
    logined_mart_index = mart_total_list.index(logined_mart)+1
    mart_p = round(logined_mart_index/mart_total_list_len*100,2)

    shopping_total_list.sort()
    shopping_total_list_len = len(shopping_total_list)
    logined_shopping_index = shopping_total_list.index(logined_shopping)+1
    shopping_p = round(logined_shopping_index/shopping_total_list_len*100,2)

    entertainment_total_list.sort()
    entertainment_total_list_len = len(entertainment_total_list)
    logined_entertainment_index = entertainment_total_list.index(logined_entertainment)+1
    entertainment_p = round(logined_entertainment_index/entertainment_total_list_len*100,2)

    medical_total_list.sort()
    medical_total_list_len = len(medical_total_list)
    logined_medical_index = medical_total_list.index(logined_medical)+1
    medical_p = round(logined_medical_index/medical_total_list_len*100,2)

    utility_total_list.sort()
    utility_total_list_len = len(utility_total_list)
    logined_utility_index = utility_total_list.index(logined_utility)+1
    utility_p = round(logined_utility_index/utility_total_list_len*100,2)

    etc_total_list.sort()
    etc_total_list_len = len(etc_total_list)
    logined_etc_index = etc_total_list.index(logined_etc)+1
    etc_p = round(logined_etc_index/etc_total_list_len*100,2)

    p_list = []
    r_p_list = []
    category_name = []
    for key in sorted_logined_consum_list.keys():
        if key == "식비":
            p_list.append(food_p)
            r_p_list.append(100-food_p)
            category_name.append("식비")
        elif key == "교통":
            p_list.append(transport_p)
            r_p_list.append(100-transport_p)
            category_name.append("교통")
        elif key == "카페.간식":
            p_list.append(snacks_p)
            r_p_list.append(100-snacks_p)
            category_name.append("카페.간식")
        elif key == "편의점.마트":
            p_list.append(mart_p)
            r_p_list.append(100-mart_p)
            category_name.append("편의점.마트")
        elif key == "쇼핑":
            p_list.append(shopping_p)
            r_p_list.append(100-shopping_p)
            category_name.append("쇼핑")
        elif key == "술.유흥":
            p_list.append(entertainment_p)
            r_p_list.append(100-entertainment_p)
            category_name.append("술.유흥")
        elif key == "의료비":
            p_list.append(medical_p)
            r_p_list.append(100-medical_p)
            category_name.append("의료비")
        elif key == "공과금":
            p_list.append(utility_p)
            r_p_list.append(100-utility_p)
            category_name.append("공과금")
        elif key == "기타":
            p_list.append(etc_p)
            r_p_list.append(100-etc_p)
            category_name.append("기타")

    return render(request, 'home.html', {'consum_list_k':sorted_logined_consum_list.keys(), 'consum_list_v':sorted_logined_consum_list.values(), 'total':logined_total, 'total_p':total_p, 'p_list0':p_list[0], 'p_list1':p_list[1], 'p_list2':p_list[2], 'p_list3':p_list[3], 'p_list4':p_list[4], 'p_list5':p_list[5], 'p_list6':p_list[6], 'p_list7':p_list[7], 'p_list8':p_list[8], 'r_p_list0': r_p_list[0], 'r_p_list1': r_p_list[1], 'r_p_list2': r_p_list[2], 'r_p_list3': r_p_list[3], 'r_p_list4': r_p_list[4], 'r_p_list5': r_p_list[5], 'r_p_list6': r_p_list[6], 'r_p_list7': r_p_list[7], 'r_p_list8': r_p_list[8], 'category_name0':category_name[0], 'category_name1':category_name[1], 'category_name2':category_name[2], 'category_name3':category_name[3], 'category_name4':category_name[4], 'category_name5':category_name[5], 'category_name6':category_name[6], 'category_name7':category_name[7], 'category_name8':category_name[8], 'today':today})
    # return render(request, 'home.html', {'consum_list_k':sorted_logined_consum_list.keys(), 'consum_list_v':sorted_logined_consum_list.values(), 'total':logined_total, 'total_p':total_p, 'food_p':food_p, 'transport_p':transport_p, 'snacks_p':snacks_p, 'mart_p':mart_p, 'shopping_p':shopping_p, 'entertainment_p':entertainment_p, 'medical_p':medical_p, 'utility_p':utility_p, 'etc_p':etc_p, 'b_food_p': 100-food_p, 'b_transport_p': 100-transport_p, 'b_snacks_p': 100-snacks_p, 'b_mart_p': 100-mart_p, 'b_shopping_p': 100-shopping_p, 'b_entertainment_p': 100-entertainment_p, 'b_medical_p': 100-medical_p, 'b_utility_p': 100-utility_p, 'b_etc_p': 100-etc_p})    
    # 카테고리(금액에 대한 내림차순),금액(금액에 대한 내림차순),모든항목 소비내역 합 반환


# 정규표현식
p = re.compile("money[0-9]+")


# 가계부 입력 view
def field(request):
    if request.user.is_authenticated == False:
        return redirect("accounting:home")

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
        exist_info = TransactionInfo.objects.filter(
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
            bank_account = BankAccount.objects.get(pk=bank_account)
            
            if ("is-income" + n) in request.POST:
                type1 = "수입"
            else:
                type1 = "지출"
            
            category = request.POST["category" + n]
            money = request.POST["money" + n]
            date = request.POST["date"]
            memo = request.POST["memo" + n]

            transaction_info = TransactionInfo.objects.create(
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

    ########## method가 GET 방식일 경우 ###############
    # 사용자 계좌 리스트 얻어오기
    user_bankAccount = BankAccount.objects.filter(user=request.user)

    today = DateFormat(datetime.now()).format("Y-m-d")
    date_list = today.split("-")
    last_date = calendar.monthrange(int(date_list[0]), int(date_list[1]))[1]

    # 일자별 총 수익, 지출 구하기
    total = []
    for i in range(1, last_date+1):
        date_list[2] = "%02d" % i
        date = "-".join(date_list)
        date_trans = list(TransactionInfo.objects.filter(user=request.user.id, date=date))
        date_income = 0
        date_expense = 0
        for d in date_trans:
            if d.type == "수입":
                date_income += d.money
            else:
                date_expense += d.money
        total.append({"date":i, "income":date_income, "expense":date_expense})

    trans = list(TransactionInfo.objects.filter(user=request.user.pk, date=today))
    return render(request, "account-field.html", {"trans" : trans, "dateString": 0, "total":total, "bankAccount":user_bankAccount})


def setField(request, dateString):
    if request.user.is_authenticated == False:
        return redirect("accounting:home")

    print(dateString)

    # 사용자 계좌 리스트 얻어오기
    user_bankAccount = BankAccount.objects.filter(user=request.user)

    date_list = dateString.split("-")
    last_date = calendar.monthrange(int(date_list[0]), int(date_list[1]))[1]

    # 일자별 총 수익, 지출 구하기
    total = []
    for i in range(1, last_date+1):
        date_list[2] = "%02d" % i
        date = "-".join(date_list)
        date_trans = list(TransactionInfo.objects.filter(user=request.user.id, date=date))
        date_income = 0
        date_expense = 0
        for d in date_trans:
            if d.type == "수입":
                date_income += d.money
            else:
                date_expense += d.money
        total.append({"date":i, "income":date_income, "expense":date_expense})

    # 지정한 날짜에 해당하는 가계부 불러오기
    trans = list(TransactionInfo.objects.filter(user=request.user.pk, date=dateString))
    return render(request, "account-field.html", {"trans" : trans, "dateString" : dateString, "total":total, "bankAccount":user_bankAccount})
