from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
def home(request):
    return HttpResponse("Hello Django")
def home1(request):
    return render(request,"home.html")
def home2(request):
    return render(request,"home1.html")
# Create your views here.
=======
from app1.models import book
# Create your views here.
def home(request):
    return HttpResponse("Hello Bye") 
def work1(request):
    return render(request,"work1.html")
def Data(request):
    k=book.objects.all()
    return render(request,"list.html",{"b":k})
>>>>>>> initial commit
