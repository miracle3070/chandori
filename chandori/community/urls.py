from django.urls import path
import community.views

app_name = 'community'

urlpatterns = [
    path('', community.views.community, name="community"),
    path('write/', community.views.write, name="write"),
    path('detail/<str:id>', community.views.detail, name="detail"),
    path('inform/', community.views.inform, name="inform"),
    path('question/', community.views.question, name="question"),
    path('detail_ques/<str:id>', community.views.detail_ques, name="detail_ques"),
    path('create/', community.views.create, name="create"),
    path('update/<str:id>', community.views.update, name="update"),
    path('updateAction/<str:id>', community.views.updateAction, name="updateAction"),
    path('delete/<str:id>', community.views.delete, name="delete"),
    path('my_content', community.views.my_content, name="my_content"),
]