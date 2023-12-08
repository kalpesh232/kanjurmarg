from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
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
        
def LoginPage(request):
    return render(request, 'login.html')

def LoginUser(request):
    if request.method == 'POST':
        account_type = request.POST['account-type']
        user_email = request.POST['user-email']
        password = request.POST['password']

        user = myUserMaster.objects.get(email=user_email)
        if user:
           if user.password == password:
               request.session['id'] = user.id
               request.session['role'] = user.role
               request.session['email'] = user.email
               if account_type == 'Candidate':
                   can = myCandidate.objects.get(user_id=user)
                   request.session['firstname'] = can.firstname
                   request.session['lastname'] = can.lastname
               else:
                   com = myCompany.objects.get(user_id=user)
                   request.session['firstname'] = com.firstname
                   request.session['lastname'] = com.lastname 
               return redirect('index_page')
           else:
            message = "Passwaord Not Registred"
            return render(request, 'login.html',{'msg' : message})
        else:
            message = "Email Not Registred"
            return render(request, 'login.html',{'msg' : message})

    else:
        return render(request, 'login.html')
    
def profile_update(request, pk):
    user = myUserMaster.objects.get(pk=pk)
    role = request.session['role']
    if role == 'candidate' :
        can_com = myCandidate.objects.get(id=pk)
    else:
        can_com = myCompany.objects.get(id=pk)
    if request.method == 'POST':
        can_com.contact = request.POST['phone_number']
        can_com.state = request.POST['state']
        can_com.city = request.POST['city']
        can_com.address = request.POST['address']
        can_com.dob = request.POST['dob']
        can_com.firstname = request.POST['firstname']
        can_com.lastname = request.POST['lastname']
        can_com.gender = request.POST['gender']
        can_com.job_title = request.POST['job_title']
        can_com.job_type = request.POST['job_type']
        can_com.job_category = request.POST['job_category']
        can_com.country = request.POST['country']
        can_com.year_of_exp = request.POST['years_of_experience']
        can_com.edu_level = request.POST['education_level']
        can_com.website = request.POST['website']
        can_com.min_salary = request.POST['min_salary']
        can_com.max_salary = request.POST['max_salary']
        can_com.job_desc = request.POST['job_description']
        # can_com.profile_pic = request.POST['profile_pic']
        can_com.shift = request.POST['shift']
        can_com.profile_pic = request.FILES['profile_photo']

        can_com.save()
        print('user.id : ', user.id)
        url = f'profile_update/{user.id}/'
        return HttpResponseRedirect(request.path_info)

    else:
        return render(request, 'profile.html',{'user' : user, 'can_com' :can_com })