from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id','title','opis']