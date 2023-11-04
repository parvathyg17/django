from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from app1.models import Book,data
from app1.forms import BookCreate

# Create your views here.
def drag(request):
    b=data.objects.all()
    return render(request,'index.html',{'b':b})


def upload(request):
    upload=BookCreate()
    if request.method=='POST':
        upload=BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href="{{url : 'index'}}"reload</a> """)
    else:
        return render(request, 'upload_form.html',{'upload_form':upload})

def index(request):
    shelf=Book.objects.all()
    return render(request, 'list.html',{'shelf':shelf})        

# def drop(request):
#     b=data.objects.all()
#     return render(request,'index.html',{'b':b})