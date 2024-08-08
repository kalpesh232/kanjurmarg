from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from . models import Employee, Role,Department
from django.db.models import Q
from django.contrib import messages
from datetime import datetime

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

        messages.success(request, "User Added Successfully")
        return redirect('add_emp')
    
    else:
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'depts' : departments,
            'rols' : roles
        }
        return render(request, 'add_emp.html',context)

def remove_emp(request, emp_id=None):
    if emp_id:
        # Retrieve the employee object or return a 404 error if not found
        print('-----------------', emp_id)
        employee = Employee.objects.get(id=emp_id)
        employee.delete()
        return redirect('remove_emp_list')  # Redirect to the list of employees or any other page
    all_users = Employee.objects.all()
    context = {
        'emps': all_users
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        all_emps = Employee.objects.all()
        
        f_l_name = request.POST['f_l_name']
        dept = request.POST['dept']
        rol = request.POST['rol']
        if f_l_name:
            all_emps = all_emps.filter(Q(first_name__icontains = f_l_name) | Q(last_name__icontains = f_l_name))
        if dept:
            all_emps = all_emps.filter(Q(dept__name__icontains = dept) )
        if rol:
            all_emps = all_emps.filter(Q(role__name__icontains = rol) )
        context = {
            'emps' : all_emps
        }
        print('--------------------', context['emps'])
        return render(request, 'view_all_emp.html', context)
    return render(request, 'filter_emp.html')

def update_emp(request, emp_id=None):
    print('-----------------', emp_id)
    if request.method == 'POST' :
        user_info = Employee.objects.get(id=emp_id)
        user_info.first_name = request.POST['f_name']
        user_info.last_name = request.POST['l_name']
        user_info.dept_id = int(request.POST['dept'])
        user_info.salary = int(request.POST['sal'])
        user_info.bonus = int(request.POST['bonus'])
        user_info.role_id = int(request.POST['role'])
        user_info.phone = int(request.POST['phone'])
        user_info.hire_date = request.POST['h_date']
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(user_info.hire_date, '%b. %d, %Y')

        # Format the datetime object into YYYY-MM-DD format
        formatted_date = date_obj.strftime('%Y-%m-%d')

        user_info.hire_date = formatted_date
        print('user_info.hire_date : ', user_info.hire_date)
        
        user_info.save()
        return redirect("view_emp")

    if emp_id:
        # Retrieve the employee object or return a 404 error if not found
        employee = Employee.objects.get(id=emp_id)
      
        depts = Department.objects.all()
        rols = Role.objects.all()

        first_name =  employee.first_name
        last_name =  employee.last_name
        dept =  employee.dept
        salary = employee.salary
        bonus =  employee.bonus
        role =  employee.role
        phone =  employee.phone
        hire_date =  employee.hire_date

        context = {
            'first_name' : first_name,
            'last_name' : last_name,
            'dept' : dept,
            'salary' : salary,
            'bonus' : bonus,
            'role' : role,
            'phone' : phone,
            'hire_date' : hire_date,
            'emp_id' : emp_id,
            'depts' : depts,
            'rols' : rols
        }

        return render(request, 'update-emp.html', context)  # Redirect to the list of employees or any other page
    all_users = Employee.objects.all()
    context = {
        'emps': all_users
    }
    return render(request, 'remove_emp.html', context)
