
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.conf.urls import include
from core import urls

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('users/')
    path('api/', include(urls)),
    path('auth/', obtain_auth_token)

]