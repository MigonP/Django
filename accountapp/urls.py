from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.conf.urls import include
from . import urls, views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout_auth,name='logout')
]
