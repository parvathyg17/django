from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello Django")
def home1(request):
    return render(request,"home.html")
def home2(request):
    return render(request,"home1.html")
# Create your views here.
