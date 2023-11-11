from django.shortcuts import render
from .models import *

# Create your views here.
def RegisterPage(request):
    return render(request,'auth_app/register.html')

def User_Register(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        image_name = request.POST['imagename']
        user_pic = request.FILES['image']

        user = UserRegister.objects.filter(Email = email)
        print('user_filter : ', user)
        if user:
            message = 'User Alraedy Exist'
            return render(request, 'auth_app/register.html', {'msg' : message})
        else:
            if password == cpassword:
                UserRegister.objects.create(Firstname = firstname, Lastname = lastname, Email = email, Phone = phone, Password = password,ImageName=image_name,pic=user_pic)
                message = 'User Successfully Created'
                return render(request, 'auth_app/login.html',{'msg':message})
            else:
                message = 'Please Check Password'
                return render(request, 'auth_app/register.html', {'msg' : message})

def UserLoginForm(request):
    return render(request, 'auth_app/login.html')

def UserLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = UserRegister.objects.get(Email=email)
        if user.Password == password:
            request.session['Firstname'] = user.Firstname
            request.session['Lastname'] = user.Lastname
            request.session['Password'] = user.Password
            request.session['ImageName'] = user.ImageName
            request.session['pic'] = str(user.pic)
            return render(request, 'auth_app/home.html')
        else:
            message = "Password doest Not Exist"
            return render(request, 'auth_app/login.html',{'msg' : message})
    else:
        message = "User doest Not Exist"
        return render(request, 'auth_app/register.html',{'msg' : message})


