<<<<<<< HEAD
"""
URL configuration for adhi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
=======
"""adhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
>>>>>>> initial commit
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
from django.urls import path
from app1 import views
<<<<<<< HEAD
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/',views.home, name='home'),
    path('',views.home1),
    path('home2/',views.home2,name='next'),
] 
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sdd/', views.home),
    path('work1/', views.work1),
    path('',views.Data),
]
>>>>>>> initial commit