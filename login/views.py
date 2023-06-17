from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
import datetime
from time import gmtime, strftime
from login.models import Attachments
from django.contrib.auth.hashers import make_password
# Create your views here.
def userLogin(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def userAuthentication(request):
    # return render(request,'')
    if(request.method=='POST') :
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = authenticate(username=username,password=pwd)

        if user is not None:
            messages.success(request,"User found successfully")
            return redirect('gallery/')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('/login')
def saveUser(request):
    if request.method == 'POST':
        username      = request.POST.get('first_name').lower()
        first_name      = request.POST.get('first_name')
        last_name       = request.POST.get('last_name')
        email           = request.POST.get('email')
        pwd             = request.POST.get('pwd')
        profile_image   = request.FILES['profile_image']
        date_joined = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        user_obj = User(username=username,first_name=first_name,last_name=last_name,password=make_password(pwd),email=email,is_staff=1,is_active=1,date_joined=date_joined)
        # print(profile_image)
        user_obj.save()
        if user_obj.pk is not None:
            image = Attachments(profile_image_url=profile_image,entity_id=user_obj.pk,entity_code='user',is_deleted=0)
            image.save()
            return  redirect('./signup')

def home(request):
    return render(request,'home.html')
