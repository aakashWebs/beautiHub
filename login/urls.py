from  django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.userLogin),
    path('login',views.userLogin),
    path('signup',views.signup),
    path('authenticateUser',views.userAuthentication),
    path('saveUser',views.saveUser),
    path('home',views.home),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)