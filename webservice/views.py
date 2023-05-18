from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.serializers import serialize
# Create your views here.
def index(request):
  users = User.objects.all()
  data = serialize('json',users)
  return HttpResponse(data,content_type='application/json')

def userDetail(request):
  user_id = request.GET.get('user_id')
  user_detail = User.objects.filter(id=user_id)
  data = serialize('json',user_detail)
  return HttpResponse(data,content_type='application/json')
