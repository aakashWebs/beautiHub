from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import userSerializer,ProfileSerializer
from login.models import Attachments
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
