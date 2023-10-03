from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signUp(request):
    return render(request,'signup.html')

def loginpage(request):
    if request.user.is_authenticated:
        return render(request,'login.html')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(homepage)
            else:
                messages.info(request,'user not exist')
                print('user not exist')
                return redirect(loginpage)
    return render(request,'login.html')


@login_required
def homepage(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect(loginpage)

@login_required
def userlogout(request):
    logout(request)
    return redirect(loginpage)