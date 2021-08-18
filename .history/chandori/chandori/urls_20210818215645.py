from django.contrib import admin
from django.urls import path
import accounting.views
urlpatterns = [
    path('admin/', admin.site.urls),
]
