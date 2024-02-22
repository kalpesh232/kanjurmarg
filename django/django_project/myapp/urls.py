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
    path('profile_update/<int:pk>/',views.profile_update,name='profileupdate'),

    # ########### comapny side ##########################

    path('company_admin/',views.companyAdmin,name='company_index'),
    path('company_profile/<int:pk>/',views.CompanyProfile,name='company_profile'),
    path('companyprofileupdate/<int:pk>/', views.CompanyProfileUpdate,name='company_user_profile'),
    path('jobpost/', views.jobPostPage, name='jobpost'),
    path('jobdetailssubmit/', views.JobDetailsSubmit, name='jobdetailssubmit')
]
