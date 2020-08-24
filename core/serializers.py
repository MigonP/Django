from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film, Rate, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True} }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
##

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('type',)

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields =('com','star', 'film')
class FilmSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    rate = RateSerializer(many=True)
    class Meta:
        model = Film
        fields = ['id','title','opis','category', 'rate','category' ]




