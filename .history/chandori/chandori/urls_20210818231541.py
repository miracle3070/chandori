from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 

import accounting.views
urlpatterns = [
    path('admin/', admin.site.urls),
]
