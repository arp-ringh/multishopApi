from django.urls import path
from .views import *
from . import views

app_name = "store"

urlpatterns = [
    path('', frontpage.as_view(), name='frontpage'),
    #path('', views.store, name='store'),
    path('contact', views.contact, name='contact'),
    #path('cart', views.cart, name='cart'),
    #path('shop', views.shop, name='shop'),
    #path('detail', views.detail, name='detail'),
    #path('checkout/', views.checkout, name='checkout'),
    #path('about', views.about, name='about'),
    #path('help', views.help, name='help'),
    #path('faqs', views.checkout, name='faqs'),
    #path('accounts/logout', views.logout, name='logout'),
]
