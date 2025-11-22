from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewset

router = DefaultRouter()
router.register('user', UserViewset)

urlpatterns = [
    path('',include('router.urls'))
]