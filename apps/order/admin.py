from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address')
    list_filter = ('email',)

@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'vendor', 'vendor_paid', 'price', 'quantity')
    list_filter = ('vendor',)
