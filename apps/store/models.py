from django.db import models
from apps.product.models import Category, Product

from django.contrib.auth.models import AbstractUser
# Create your models here.


# Create Model for below:
# Sliders
# Special Offers
STATUS = (('active', 'active'), ('', 'default'))
RANK = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))


class Offer(models.Model):
    name = models.CharField(max_length=300)
    offer_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    rank = models.CharField(choices=RANK, max_length=50)
    image = models.ImageField(upload_to='offer')

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='slider')
    url = models.CharField(max_length=500)
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS, blank=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=400, blank=True)
    subject = models.CharField(max_length=400)
    message = models.TextField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
