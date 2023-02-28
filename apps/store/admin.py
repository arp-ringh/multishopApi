from django.contrib import admin
from .models import Slider, Offer, CustomUser

# Register your models here.

#@admin.register(Slider)
#class SliderAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Slider)
admin.site.register(Offer)
admin.site.register(CustomUser)
