from django.urls import path
from .views import test_select, test_prefetch

urlpatterns = [
    path("select/", test_select),
    path("prefetch/", test_prefetch),
]