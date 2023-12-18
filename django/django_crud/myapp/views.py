from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def IndexView(request):
    return render(request, 'myapp/index.html')

def FormView(request):
    return render(request,'myapp/form.html')

def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    newuser = Student.objects.create(Firstname = fname, Lastname = lname, Email = email, Contact = contact)

    return redirect('ShowPage')

def ShowPage(request):
    all_user = Student.objects.all()
    print('all_user : ',all_user)
    return render(request, 'myapp/show.html',{'key1':all_user})

def EditPage(request, pk):
    user_data = Student.objects.get(id=pk)
    print('user_data : ', user_data)
    return render(request, 'myapp/edit.html',{'key2' : user_data})

def UpdateInfo(request, pk):
    user_info = Student.objects.get(id=pk)
    user_info.Firstname = request.POST['fname']
    user_info.Lastname = request.POST['lname']
    user_info.Email = request.POST['email']
    user_info.Contact = request.POST['contact']
    user_info.save()
    return redirect('ShowPage')

def DeleteRecord(request,pk):
    delete_record = Student.objects.get(id=pk)
    delete_record.delete()
    return redirect('ShowPage')

