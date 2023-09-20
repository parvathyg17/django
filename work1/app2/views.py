from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from app2.forms import CustomUserCreationForm
def home(request):
    return HttpResponse("Hello Django")
def home(request):
    return render(request,'home.html')
def base(request):
    return render(request,'base.html')
def signUp1(request):
    form=CustomUserCreationForm()
    if(request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'signup1.html',{"form":form})
def user_login1(request):
    if(request.method=="POST"):
        name=request.POST['n']
        password=request.POST['p']
        user=authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('invalid ...no user found')
    return render(request,'login1.html')
def user_logout1(request):
    logout(request)
    return user_login1(request)

def pw_change_form(request):
    return render(request,'password_change_form.html')

def pw_change_done(request):
    return render(request,'password_change_done.html')