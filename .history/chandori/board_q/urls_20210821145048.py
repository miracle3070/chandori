from django.urls import path
import board_q.views

app_name = 'board_q'

urlpatterns = [
    path('', board_q.views.board2, name="board2"),
]