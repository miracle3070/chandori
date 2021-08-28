from django.db import models
from account.models import * #account에 있는 CustomUser를 가져옴

class consum(models.Model):
    #  사용자 정보
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)#  Foeign Key 설정, on_delete 설정 : 참조한 키가 삭제되면 그 키와 관련된 데이터를 같이 삭제해주세요

    #언제 썻는지?
    date = models.DateTimeField('date published')

    #어떠한 항목을?
    category1 = "식비"
    category2 = "교통비"
    category3 = "카페&간식"
    category4 = "편의점&마트"
    category5 = "쇼핑"
    category6 = "술&유흥"
    category7 = "의료비"
    category8 = "공과금"
    category9 = "기타"
    categoryset = ((category1, "식비"),(category2, "교통비"),(category3, "카페&간식"),(category4, "편의점&마트"),(category5, "쇼핑"),(category6, "술&유흥"),(category7, "의료비"),(category8, "공과금"),(category9, "기타"))
    category = models.CharField(choices=categoryset, max_length=10, null= True, blank=True)
    
    #얼마 만큼?
    money = models.IntegerField(null= True, blank=True)
