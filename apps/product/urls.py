from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('<slug:category_slug>', views.category, name='category'),
    path('<slug:category_slug>/<slug:subcategory_slug>', views.subcategory, name='subcategory'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name='product'),
    path('product/<slug:category_slug>/<slug:product_slug>', views.product, name='product'),
    path('search/', views.search, name='search'),

    ]
