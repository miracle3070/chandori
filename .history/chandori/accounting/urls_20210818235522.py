from django.urls import path
import accounting.views

urlpatterns = [
    path('', accounting.views.index)
]