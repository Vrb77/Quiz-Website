"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from quiz_app import views

from django.conf.urls import url, include


urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    #path('login1',views.login1,name='login1'),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('phy',views.phy,name='phy'),
    path('p1',views.p1,name='p1'),
    path('p2',views.p2,name='p2'),  
    path('addp1',views.addp1,name='addp1'),
    path('addp2',views.addp2,name='addp2'),

    path('math',views.math,name='math'),
    path('m1',views.m1,name='m1'),
    path('m2',views.m2,name='m2'),  
    path('addm1',views.addm1,name='addm1'),
    path('addm2',views.addm2,name='addm2'),

    path('bio',views.bio,name='bio'),
    path('b1',views.b1,name='b1'),
    path('b2',views.b2,name='b2'),  
    path('addb1',views.addb1,name='addb1'),
    path('addb2',views.addb2,name='addb2'),
    
    path('chem',views.chem,name='chem'),
    path('c1',views.c1,name='c1'),
    path('c2',views.c2,name='c2'),  
    path('addc1',views.addc1,name='addc1'),
    path('addc2',views.addc2,name='addc2'),
  
   
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),  
    path('logout/', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),

    
]