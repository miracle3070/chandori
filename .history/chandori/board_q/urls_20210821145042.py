from django.urls import path
import board_info.views

app_name = 'board_q'

urlpatterns = [
    path('', board_info.views.board2, name="board2"),
]