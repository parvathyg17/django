from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import employee
from app1.forms import employeeForm


def list(request):
    k=employee.objects.all()
    return render(request,'list.html',{"f":k})

def form1(request):
    if(request.method=='POST'):
        i=request.POST['i']
        n=request.POST['n']
        d=request.POST['d']
        s=request.POST['s']
        o=employee.objects.create(e_id=i,ename=n, emp_dep=d,emp_salary=s)
        o.save()
        return list(request)
    return render(request,'form.html')