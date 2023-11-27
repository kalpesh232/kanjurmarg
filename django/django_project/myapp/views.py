from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
import random

# Create your views here.

def IndexPage(request):
    return render(request, 'index.html')

def SignPage(request):
    return render(request, 'signup.html')

def Registration(request):
    if request.method == 'POST':
        fname = request.POST['first-name']
        lname = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm-password']
        role = request.POST['account-type']
        user = myUserMaster.objects.filter(email=email)
        if user:
            return render(request, 'signup.html', {'msg' : 'User Already Exist'})
        else:
            if cpassword == password:
                otp = random.randint(100000,999999)
                newuser = myUserMaster.objects.create(email=email, password=password,otp=otp,role=role)
                if role == "candidate":
                    myCandidate.objects.create(user_id=newuser, firstname=fname, lastname =lname)
                else:
                    myCompany.objects.create(user_id=newuser,firstname=fname, lastname =lname)
                return render(request, 'otpverify.html', {'email':email})
            else:
                 return render(request, 'signup.html', {'msg' : 'Check Password and Confirm Password'})
            
def OTPPage(request):
    return render(request, 'otpverify.html')

def OTPVerify(request):
    if request.method == 'POST':
        email = request.POST['user-email']
        otp = int( request.POST['otp'])
        print('email : ', email)
        
        user = myUserMaster.objects.get(email=email)
        print('user : ', user)
        if user :
            if user.otp == otp:
                message = 'OTP Verified Successfully'
                return render(request, 'login.html', {'msg' : message})
            else:
                message = 'OTP is Incorrect'
                return render(request, 'otpverify.html', {'msg' : message})
        else:
            message = 'User Not Found'
            return render(request, 'signup.html', {'msg' : message})
