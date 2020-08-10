
from django.conf.urls import include, url
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'filmy', views.FilmViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),

]