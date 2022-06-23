from unicodedata import category
from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=100)
    amount = models.PositiveSmallIntegerField()
    shop = models.ForeignKey(
        Shop, on_delete=models.DO_NOTHING, related_name="product_shop"
    )
    category = models.ManyToManyField(Category,related_name="product_category")
    price = models.FloatField()
    image = models.ImageField(upload_to="uploads/")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
