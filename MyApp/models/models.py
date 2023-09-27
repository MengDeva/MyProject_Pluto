import datetime
from django.db import models


# Create your models here.
class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)
    createBy = models.IntegerField(null=True, blank=True)
    updateBy = models.IntegerField(null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=datetime.datetime.now())
    updateAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    barcode = models.BigIntegerField(null=True, unique=True)
    unitPrice = models.FloatField()
    qtyInstock = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="media/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createBy = models.IntegerField(null=True, blank=True)
    updateBy = models.IntegerField(null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=datetime.datetime.now())
    updateAt = models.DateTimeField(null=True, blank=True)

# class User(models.Model):
#     username = models.CharField()
#     date = models.DateTimeField()
