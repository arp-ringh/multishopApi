from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



from apps.store.models import CustomUser
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        return user
