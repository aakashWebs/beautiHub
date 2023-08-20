from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from login.models import Attachments
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import requests
from django.http import JsonResponse
import json
from beautiHub.utils import *

# Create your views here.
def addProfiles(request):
    if request.method == 'POST':
        name =  request.POST.get('name')
        age =  request.POST.get('age')
        description = request.POST.get('description')
        # profile_image = request.FILES['profile_image']
        # user_id = request.user.id
        user = User.objects.get(id=4)
        # print('user_id',user)
        # print('user',user)
        # return False;
        # print("sdfjkshfjksdfkj")
        # print('aksdjasdjasdhj',request.FILES.getlist("profile_image"))
        # return false;
        # profile_image = request.FILES['profile_image']
        profile_image = request.FILES.getlist("profile_image")
        profile_data = Profile(name=name,age=age,description=description,added_by=user)
        profile_data.save()
        if profile_data.pk is not None:
            for p_img in profile_image:
                image = Attachments(profile_image_url=p_img, entity_id=profile_data.pk, entity_code='profile',
                                is_deleted=0)
                image.save()

        return redirect('../gallery/add_profiles')
    return render(request,'gallery/profile.html')

def profiles(request):
    # response = requests.get('http://127.0.0.1:8000/api/get_profile_list/')
    api_params = {
        'entity_id':11,
        'entity_code':'profile'
        }
    response = callRestApi('get_attachments',api_params)
    data = []
    if response['settings']['success']:
        data = response['data']
    return render(request, 'home.html', {'data': data})

def userProfile(request,id):
    api_params = {
        'entity_id': id,
        'entity_code': 'profile'
    }
    user_param = {
        'user_id':id
    }
    user_data = callRestApi('get_profile',user_param)
    response = callRestApi('get_attachments', api_params)
    data = []
    if response['settings']['success']:
        data = response['data']

    return render(request, 'home.html', {'data': data})

def userList(request):
    # base_url = request.build_absolute_uri('/')[:-1]
    context = {
        'iterator': range(1, 5),
        # 'base_url':base_url
    }
    return render(request,'gallery/user_list.html',context)

def getUsers(request):
    data = []
    response = callRestApi('get_profile_list',{})
    if response['settings']['success']:
        data = {'data':response['data']}
    # print('data',data)
    return JsonResponse(data,safe=False)