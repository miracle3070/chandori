from django.urls import path
import accounting.views

urlpatterns = [
    path('', views.index)
]