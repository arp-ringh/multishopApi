from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



from apps.store.models import CustomUser
from apps.product.models import Product
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class VendorSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        if commit:
            user.save()
        return user


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = [
                  'name',
                  'category',
                  'subcategory',
                  'labels',
                  'price',
                  'discounted_price',
                  'image',
                  'description',
                  'overview',

                  ]
