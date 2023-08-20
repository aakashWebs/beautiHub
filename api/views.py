from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import userSerializer, ProfileSerializer, profileSerializer,userLoginSerializer
from login.models import Attachments
from rest_framework.exceptions import APIException, NotFound
from gallery.models import Profile
from collections import defaultdict
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



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
    data = []
    try:
        profiles = Profile.objects.all()
        settings = {'success': 1, 'message': 'Data Found Successfully'}
    except Profile.DoesNotExist:
        profiles = None
        settings = {'success': 0,'message': 'Data Not Found'}

    if profiles is not None:
        serializer = profileSerializer(profiles, many=True)
        data       = serializer.data
    return_obj = {'settings':settings,'data':data}
    return Response(return_obj)

@api_view(['GET','POST'])
def getProfile(request):
    user_id = request.query_params.get('user_id')
    profile = get_object_or_404(Profile, id=user_id)
    settings = {'success': 0, 'message': 'Data Not Found'}
    data = []
    if profile is not None:
        serializer = profileSerializer(profile)
        data       = serializer.data
        settings = {'success': 1, 'message': 'Data Found Successfully'}
    return_obj = {'settings':settings,'data':data}
    return Response(return_obj)
@api_view(['GET','POST'])
def getAttachments(request):
    data = []
    entity_id   = request.query_params.get('entity_id')
    entity_code = request.query_params.get('entity_code')
    attachments = Attachments.objects.filter(entity_id=entity_id, entity_code=entity_code,
                                             profile_image_url__isnull=False).values('profile_image_url')
    settings = {'success':0, 'message': 'Data Not Found'}
    if attachments:
        attachments_list = list(attachments)
        img_arr = defaultdict(list)
        # for i in attachments_list:
        #     img_arr[i['entity_id']].append(i['profile_image_url'])
        data = attachments_list
        settings = {'success': 1, 'message': 'Data Found Successfully'}

    return_obj = {'settings':settings,'data': data}
    return Response(return_obj)
@api_view(['GET','POST'])
def userLogin(request):
        # username = request.query_params.get('username')
        # password = request.query_params.get('password')

        user_data = userLoginSerializer(data=request.query_params)
        if user_data.is_valid():
            # Validated data is available in serializer.validated_data
            username = user_data.validated_data['username']
            password = user_data.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                settings = {'success': 1, 'message': 'Data Found Successfully..!'}
                user_obj = User.objects.get(username= user_data.data['username'])
                refresh = RefreshToken.for_user(user_obj)
                data = [{'access_token':str(refresh.access_token)}]
            else:
                settings = {'success': 0, 'message': 'Data Not Found'}
                data = []

            return_data = {'settings':settings,'data':data}
            return Response(return_data)
        else:
            return Response(user_data.errors, status=400)
