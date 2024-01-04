from django.db import models
from Admin.models import *

# Create your models here.
class newuser(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to='UserDocs/')
    password=models.CharField(max_length=50,unique=True)


class Seller(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    logo=models.FileField(upload_to='Sellerlogo/')
    proof=models.FileField(upload_to='Sellerproof/')
    password=models.CharField(max_length=50,unique=True)
    doj=models.DateField(auto_now=True)
    vstatus=models.IntegerField(default=0)