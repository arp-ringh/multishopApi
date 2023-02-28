"""
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor

# Create your views here.

def vendor_apply(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('store:frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/vendor-apply.html', {'form':form})

"""


from django.shortcuts import render, redirect
from apps.store.models import CustomUser
from apps.vendor.models import Vendor
from django.views.generic import CreateView, View

from django.contrib.auth import login, logout
from django.contrib import messages, auth

from apps.vendor.decorators import vendor_required
from django.contrib.auth.decorators import login_required

from .forms import VendorSignUpForm, ProductForm
from django.utils.text import slugify

from apps.product.models import Product
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.

class vendorSignUpView(CreateView):
    model = CustomUser
    form_class = VendorSignUpForm
    template_name = 'registration/vendor_register.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        vendor = Vendor.objects.create(name=user.username,created_by=user)
        return redirect('vendor:vendordash')


"""
# For class based views this is how decorators should be wrapped

decorators = [
                login_required,
                vendor_required,
              ]

@method_decorator(decorators, name='dispatch')
"""

@login_required
@vendor_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.name)
            product.save()

            return redirect('vendor:vendordash')
    else:
        form = ProductForm()
    return render(request, 'vendor/add_product.html', {'form':form})


@login_required
@vendor_required
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)

    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        product.save()
        return redirect('vendor:vendordash')

    return render(request, 'vendor/update_product.html', {'form':form, 'product':product})


@login_required
@vendor_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    #product.delete()

    if request.user.vendor == product.vendor:
        product.delete()

    return redirect('vendor:vendordash')

"""
@login_required
@vendor_required
def vendorDash(request):
    #views = {}
    vendor = request.user.vendor
    products = vendor.products.all()

    return render(request, 'vendor/vendor-dash.html',{'vendor':vendor, 'products':products})
"""


from django.core.paginator import Paginator
@login_required
@vendor_required
def vendorDash(request):
    vendor = request.user.vendor
    query = vendor.products.all()
    paginator = Paginator(query,10)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'vendor/vendor-dash.html',{'vendor':vendor, 'products':products})
