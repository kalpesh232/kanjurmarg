from django.shortcuts import render, HttpResponse
from . models import Employee, Role,Department

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    print(emps)
    context = {
        'emps' : emps
    }
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST' :
        
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['sal'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['h_date']

        new_user = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=hire_date)
        new_user.save()

        context = {
            'msg' : "User Added Successfully"
        }
        return render(request, 'add_emp.html',context)

        print('____________request is post_________________', hire_date)
    else:
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'depts' : departments,
            'rols' : roles
        }
        return render(request, 'add_emp.html',context)

def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')
