"""
URL configuration for work1 project.

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
from app2 import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    path('logout1/',views.user_logout1,name='logout1'),
    path('',views.home,name='home'),
    path('sigup',views.signUp1,name='signup1'),
    path('login1/',views.user_login1,name='login1'),
    path('/as',views.pw_change_form),
    path('aj/',views.pw_change_done),
]
