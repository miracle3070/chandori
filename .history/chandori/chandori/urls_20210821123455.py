from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from django.conf.urls import url
import accounting.views

urlpatterns = [
    path('', include('accounting.urls')),
    path('accounting', include('accounting.urls')),
    path('admin/', admin.site.urls),
]
