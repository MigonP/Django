
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer
from .models import Film, Rate
from .serializers import FilmSerializer, RateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from django.shortcuts import render
from .models import *
from VideoApp.models import *
from VideoApp.froms import CrateVid
def FPage(request):
    auth_usr = request.user
    context ={
        'usr':auth_usr
    }
    return render(request, 'FPage.html', context)

def ShowMeApp(request):
    auth_usr = request.user
    obj = UploadVideoModel.objects.all()
    context = {
        'usr': auth_usr,
        'obj': obj
    }
    return render(request, 'clip.html',context)

def CreateVid(request):
    form = CrateVid(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'Create_video.html', {'form':form})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)



class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    #authentication_classes = (TokenAuthentication, )
    #permission_classes = (DjangoModelPermissions,)


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


