from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.RegisterPage, name='registerpage' ),
   path('register_user', views.User_Register, name='userregister'),
   path('login_form', views.UserLoginForm, name='login_form'),
   path('user_login', views.UserLogin, name='user_login')
]