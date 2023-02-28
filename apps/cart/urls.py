from django.urls import path
#from .views import *
from . import views

app_name = "cart"

urlpatterns = [
    path('cart/', views.cart_detail, name='cart'),
    path('cart/checkout/', views.cart_checkout, name='checkout'),
    path('success/', views.checkout_success, name='success'),
    ]
