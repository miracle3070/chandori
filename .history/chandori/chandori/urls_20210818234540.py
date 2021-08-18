from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 

import accounting.views
urlpatterns = [
    path('', include('accounting.urls')),
    path('admin/', admin.site.urls),
]
