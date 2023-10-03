from django.shortcuts import render,redirect
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

def edit_emp(request,pk):
    employe=employee.objects.get(id=pk)
    form=employeeForm(instance=employe)
    if request.method=='POST':
        form=employeeForm(request.POST,instance=employe)
        if form.is_valid():
            form.save()
            return redirect('list')
    context={
        'employee':employe,
        'form':form,
    }
    return render(request,'edit.html',context)
def del_emp(request,pk):
    emploe=employee.objects.get(id=pk)
    if request.method=='POST':
        emploe.delete()
        return redirect('list')
    context={
        'employee':emploe,
    }
    return render(request,'delete.html',context)
def view_emp(request,pk):
    emploe=employee.objects.get(id=pk)
    return render(request,'view.html',{"employee":emploe})



 