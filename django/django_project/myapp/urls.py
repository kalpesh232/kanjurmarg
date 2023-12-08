from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.IndexPage,name='index_page'),
    path('signup/',views.SignPage,name='signup_page'),
    path('register',views.Registration,name='register'),
    path('otp',views.OTPPage,name='otp'),
    path('otpverify',views.OTPVerify,name='otpverify'),
    path('login/',views.LoginPage,name='loginpage'),
    path('loginuser/',views.LoginUser,name='loginuser'),
]