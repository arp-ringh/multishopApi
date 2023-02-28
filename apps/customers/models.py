from apps.store.models import CustomUser
from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.OneToOneField(CustomUser, related_name='customer', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


