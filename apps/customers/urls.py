from django.urls import path
from .views import *
from . import views

app_name = "customers"

urlpatterns = [
    path('accounts/register/customer/', customerSignUpView.as_view(), name='customer'),
    path('dashboard/customer/', views.customerDash, name='customerdash'),

]
