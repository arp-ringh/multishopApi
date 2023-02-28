"""
from django.urls import path
from django.contrib.auth import views as auth_views
#from .views import *
from . import views

app_name = "vendor"

urlpatterns = [
    path('vendor-apply/', views.vendor_apply, name='vendor-apply'),
    path('vendor-login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),

    ]
"""


from django.urls import path
from .views import *
from . import views

app_name = "vendor"

urlpatterns = [
    path('accounts/register/vendor/', vendorSignUpView.as_view(), name='vendor'),
    path('dashboard/vendor/', views.vendorDash, name='vendordash'),
    path('vendor/product/add/', views.add_product, name='product-add'),
    path('vendor/product/<product_id>/update/', views.update_product, name='product-update'),
    path('vendor/product/<product_id>/delete/', views.delete_product, name='product-delete'),

]
