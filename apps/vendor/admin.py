from django.contrib import admin

# Register your models here.

from .models import  Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name',)
