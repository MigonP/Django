from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login as auth_login, logout
from VideoApp.models import UploadVideoModel,UsrRegModel


def register(request):
    if request.method == 'POST':
        form_usr = UserCreationForm(request.POST)
        if form_usr.is_valid():
            usr=form_usr.save()
            login(request, usr)
            return redirect('/')
    else:
        form_usr = UserCreationForm()

    context = {
        'form_usr' : form_usr,
    }
    return render(request, 'accountapp/register.html', context)




def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print('post')
        if form.is_valid():
            print('valid')
            auth_login(request, form.get_user())
            print('logedin')
            return redirect('/')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accountapp/login.html', context)

def logout_auth(request):
    logout(request)
    return redirect('login')


def user_details(request, id=id):
    usr_obj = UsrRegModel.objects.get(root_user__username=int(id))
    vid_obj = UploadVideoModel.objects.filter(root_user__username=int(id))
    context = {
        'obj':usr_obj,
        'vid_obj': vid_obj,
    }
    return render(request, 'user_details.html',context)

def user_details_video(request, id=id):
    usr_obj = UsrRegModel.objects.get(root_user__username=int(id))
    vid_obj = UploadVideoModel.objects.filter(root_user__username=int(id))
    context = {
        'obj': usr_obj,
        'vid_obj': vid_obj,
    }
    return render(request, 'user_details_video.html', context)