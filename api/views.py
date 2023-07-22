from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import userSerializer,ProfileSerializer,profileSerializer
from login.models import Attachments
from rest_framework.exceptions import APIException, NotFound
from gallery.models import Profile
from collections import defaultdict

import json

# Create your views here.
@api_view(['GET'])
def getUsers(request):
    dict={
        'Name':'Aakash Yadav',
        'Age':'23'
    }
    # user_data = User.objects.values()
    user_data = User.objects.all()
    id_list = list(user_data.values_list('id', flat=True))
    print('id_list',id_list)
    values_list = Attachments.objects.filter(entity_id__in=id_list).values('entity_id', 'profile_image_url')
    # print('value_list',values_list)
    # json_data = json.dumps(atment)  # Serialize to JSON
    serializer = userSerializer(user_data,many=True)
    serializer_at = ProfileSerializer(values_list,many=True)
    data = {'users_detail':serializer.data,'attachments':serializer_at.data}
    return Response(data)
    # return JsonResponse('I Am API Response',safe=False)

@api_view(['GET'])
def getUserProfile(request,id):
    try:
        user_data = get_object_or_404(User,id=id)
        data = {
        'id':id,
        'username':user_data.username,
        'email':user_data.email,
        }
        return Response(data)
    except NotFound:
        raise APIException("User not found ")
@api_view(['POST'])
def updateUser(request,pk):
        user_data = User.objects.get(id=pk)
        serializer = userSerializer(instance=user_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET','POST'])
def getProfileList(request):
    profiles = Profile.objects.all()
    id_list = list(profiles.values_list('id', flat=True))
    values_list = Attachments.objects.filter(entity_id__in=id_list).filter(entity_code='profile').filter(profile_image_url__isnull=False).values('entity_id', 'profile_image_url')
    serializer = profileSerializer(profiles, many=True)
    attachment_list = defaultdict(list)
    for val in values_list:
        attachment_list[val['entity_id']].append(val['profile_image_url'])
    data = {'profile_list':serializer.data,'attachments':attachment_list}
    return Response(data)