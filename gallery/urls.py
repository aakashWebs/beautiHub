from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.profiles),
    path('add_profiles',views.addProfiles),
    path('user_list',views.userList),
]
