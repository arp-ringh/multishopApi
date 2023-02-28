from django.shortcuts import render

from apps.store.models import CustomUser
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View

from django.contrib.auth import login, logout
from django.contrib import messages, auth

from apps.customers.models import Customer
from apps.customers.decorators import customer_required
from django.contrib.auth.decorators import login_required

from .forms import CustomerSignUpForm
# Create your views here.

class customerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_register.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        customer = Customer.objects.create(name=user.username,created_by=user)
        return redirect('customers:customerdash')


@login_required
@customer_required
def customerDash(request):
    views = {}

    #return redirect('cart:checkout')
    return render(request, 'customers/customer-dash.html', views )
