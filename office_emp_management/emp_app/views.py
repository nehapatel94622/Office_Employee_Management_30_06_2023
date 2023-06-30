from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'base.html')

def view_all(request):
    emp = Employee.objects.all()
    context = {
        'emps':emp
    }
    return render(request, 'view_all_employee.html', context)

def add_emp(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(fname=fname, lname=lname, dept_id=dept, salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added Successfully")
    elif request.method =="GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Exception Accurance! Employee has been not Added")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
           emp_delete = Employee.objects.get(id=emp_id)
           emp_delete.delete()
           return HttpResponse("Data Deleted")
        except:
            return HttpResponse("Please Enter Valid Email_Id")

    emp = Employee.objects.all()
    context = {
        'emps':emp
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method=='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(fname__icontains = name) | Q(lname__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        
        context = {
            'emps': emps
        }
        return render(request, 'view_all_employee.html', context)
        print("dfdjfnas")

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse("An Exception occur")
