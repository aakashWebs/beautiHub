from django.urls import path,include
from .views import *
urlpatterns = [
    path('',getUsers),
    path('get_user_profile/<str:id>/',getUserProfile),
    path('update_user_profile/<str:pk>/',updateUser),
    path('get_profile_list/',getProfileList),
]