from django.urls import path
import accounting.views

app_name = 'accounting'

urlpatterns = [
    path('', accounting.views.index, name="home"),
]