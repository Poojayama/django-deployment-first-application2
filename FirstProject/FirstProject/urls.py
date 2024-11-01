"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from FirstApp import views
from MultiViewsApp import views as v1
#Approch1
from App1 import views as v11
from App2 import views as v22
#Approch2
from App1.views import f11
from App2.views import f22


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.display),
    path('welcome2/',views.show),
    path('hello/', views.hello),
    path('dtime/',views.senddatetime),
    #MultiViewsApp Urls
    path('mrng/',v1.f1),
    path('afrn/',v1.f2),
    path('evng/',v1.f3),
    #Approach1-urls
    path('hello2/', v11.f11),
    path('datetime/', v22.f22),
    #Approch2-urls
    path('hello3/',f11),
    path('datetime3/',f22),
    #multi-urls same view function
    path('firstdemo/',views.demo),
    path('seconddemo/',views.demo),
    path('thirddemo/',views.demo),
    #Default-homepage-urls
    re_path("^.*$",views.homepage),
]
