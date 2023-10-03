from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import student
from app1.forms import studentForm


def form1(request):
    form=studentForm()
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list1(request)
        else:
            form=studentForm()
    return render(request,'form1.html',{"form":form})

def list1(request):
    k=student.objects.all()
    return render(request,'list.html',{"s":k})

def form2(request):
    if(request.method=='POST'):
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list1(request)
    return render(request,'form2.html')

def form3(request):
    if(request.method=='POST'):
        n=request.POST['n']
        a=request.POST['a']
        o=student.objects.create(name=n, age=a)
        o.save()
        return list1(request)
    return render(request,'form3.html')



