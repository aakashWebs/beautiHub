"""
URL configuration for beautiHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from beautiHub.middleware import metrics


urlpatterns = [
    path('metrics/', metrics),
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('webservice',include('webservice.urls')),
    path('gallery/',include('gallery.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api/',include('api.urls')),
    path('favicon.ico', serve, {'document_root': 'static/images', 'path': 'favicon.ico'}),
]
