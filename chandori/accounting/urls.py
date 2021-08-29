from django.urls import path
import accounting.views

app_name = 'accounting'

urlpatterns = [
    path('', accounting.views.home, name="home"),
    path('field/', accounting.views.field, name="field"),
    path('field/<str:dateString>', accounting.views.setField, name="setField"),
]