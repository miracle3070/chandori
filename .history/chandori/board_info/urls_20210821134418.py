from django.urls import path
import board_info.views

app_name = 'board_info'

urlpatterns = [
    path('', board_info.views.board, name="board"),
]