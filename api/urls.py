from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('',getUsers),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_user_profile/<str:id>/',getUserProfile),
    path('update_user_profile/<str:pk>/',updateUser),
    path('get_profile_list/',getProfileList),
    path('get_profile',getProfile),
    path('get_attachments',getAttachments),
    path('user_login',userLogin)
]