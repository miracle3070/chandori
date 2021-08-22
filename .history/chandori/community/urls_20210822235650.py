from django.urls import path
import community.views

app_name = 'community'

urlpatterns = [
    path('', community.views.board, name="board"),
]