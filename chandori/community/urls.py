from django.urls import path
import community.views

app_name = 'community'

urlpatterns = [
    path('', community.views.community, name="community"),
    path('write/', community.views.write, name="write"),
    path('detail/', community.views.detail, name="detail"),
    path('inform/', community.views.inform, name="inform"),
    path('question/', community.views.question, name="question"),
    path('detail_ques/', community.views.detail_ques, name="detail_ques"),
    path('create/', community.views.create, name="create"),
]