from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("details/",views.subscription_details,name="subscription_details"),
    path("action/<int:cost>", views.perform_action,name="perform_action"),
    path("recharge/", views.recharge_credits, name="recharge_credits"),
    path("signup/", views.signup, name="signup"),
    path("accounts/profile/", views.profile, name="profile"),
]

