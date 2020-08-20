
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer
from .models import Film
from .serializers import FilmSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (DjangoModelPermissions,)