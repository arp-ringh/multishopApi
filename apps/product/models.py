from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.

CAT_STAT = (('active', 'active'), ('', 'default'))
FEATURED = (('featured', 'Featured'), ('offer', 'Offer'), ('', 'Default'))


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category/images")
    status = models.CharField(choices=CAT_STAT, blank=True, max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField(upload_to="subcategory/images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='products', blank=True, null=True, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, unique=True)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    description = models.TextField()
    overview = models.TextField()
    #labels = models.CharField(choices)
    labels = models.CharField(max_length=50, choices=FEATURED, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    #vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendor.Vendor', related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/images", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="product/thumbnails", blank=True, null=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(500,500)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
