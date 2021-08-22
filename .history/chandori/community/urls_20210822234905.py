from django.urls import path
import board_info.views

app_name = 'community'

urlpatterns = [
    path('', board_info.views.community, name="commnity"),
]