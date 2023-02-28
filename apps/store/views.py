from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View

from django.contrib.auth import login, logout
from django.contrib import messages, auth

from django.core.mail import EmailMessage

from . models import *

from apps.product.models import Product

# Create your views here.

# Create views for Front Page
# Enlist Categories
# Enlist Sub Categories
# Show Slider
# Show special offers
# Show Featured Products
# Show Recently Added Products(newest product)


class BaseView(View):
    views = {}


class frontpage(BaseView):
    def get(self, request):
        self.views['slider'] = Slider.objects.all()
        self.views['offer_first'] = Offer.objects.all()[0:2]
        self.views['offer_second'] = Offer.objects.all()[2:4]


        # self.views['featured_products'] = Product.objects.filter(labels= 'featured')
        # self.views['recent_products'] = Product.objects.filter(labels= '')[0:8]

        featured_products = Product.objects.filter(labels= 'featured')[0:8]
        # self.views['featured_products'] = get_object_or_404(featured_products)
        if featured_products.exists():
            self.views['featured_products'] = get_list_or_404(featured_products)

        recent_products = Product.objects.filter(labels= '')[0:8]
        if recent_products.exists():
            self.views['recent_products'] = get_list_or_404(recent_products)

        #return render(request, 'store/frontpage.html',self.views)

        # Check if a user is logged in and is authenticated for views
        if request.user.is_authenticated:
            """
            if request.user.is_customer:
                return redirect('customers:customerdash')
            elif request.user.is_vendor:
                return redirect('vendor:vendordash')
            else:
                return redirect('admin/')
            """

            if request.user.is_vendor:
                return redirect('vendor:vendordash')
            elif request.user.is_superuser:
                return redirect('admin/')
            else:
                return render(request, 'store/frontpage.html',self.views)

        else:
            return render(request, 'store/frontpage.html',self.views)

"""
def store(request):
    views = {}
    return render(request, 'index.html', views)
"""
"""

def contact(request):
    views = {}
    return render(request, 'store/contact.html', views)

def cart(request):
    views = {}
    return render(request, 'store/cart.html', views)

def shop(request):
    views = {}
    return render(request, 'store/shop.html', views)

def detail(request):
    views = {}
    return render(request, 'store/detail.html', views)

def checkout(request):
    views = {}
    return render(request, 'store/checkout.html', views)

def about(request):
    views = {}
    return render(request, 'store/about.html', views)

def help(request):
    views = {}
    return render(request, 'store/help.html', views)

def faqs(request):
    views = {}
    return render(request, 'store/faqs.html', views)
"""


def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        data.save()

    try:
        email = EmailMessage('Hello', 'Thanks! For Messaging Us, We will get back to you soon.', 'arpringh@zohomail.com', [email])
        email.send()
    except:
        pass
    else:
        messages.success(request,'Email has sent !')
        return redirect('store:frontpage')


    return render(request, 'store/contact.html')









#######################################
## FOR API ############################
# ViewSets define the view behavior.



from rest_framework import routers, serializers, viewsets
from .serializers import *
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#########################################
## Generic

import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)
    filter_fields = ['id','name','price','labels','category','subcategory']
    ordering_fields = ['price','category','id']
    search_fields = ['name','description','overview']
