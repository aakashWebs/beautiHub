from django.urls import path,include
from . import views
urlpatterns = [
    path('/get_user_list',views.index),
    path('/get_user_detail/',views.userDetail),
]
