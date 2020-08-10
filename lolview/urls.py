
from django.contrib import admin

from django.urls import  path
from django.conf.urls import include
from core import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]