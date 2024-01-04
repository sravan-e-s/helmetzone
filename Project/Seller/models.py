from django.db import models
from Admin.models import *
from Guest.models import *
from User.models import Booking,Cart
# Create your models here.
class Delevery(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='DeleveryDocs/')
    password=models.CharField(max_length=50,unique=True)
    seller=models.ForeignKey(Seller,on_delete=models.SET_NULL,null=True)


class productt(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    details=models.EmailField(max_length=100)
    model=models.ForeignKey(helmetModels,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='productDocs/')
    seller=models.ForeignKey(Seller,on_delete=models.SET_NULL,null=True)


class Workassign(models.Model):
    dboy=models.ForeignKey(Delevery,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)
    cid=models.ForeignKey(Cart,on_delete=models.CASCADE)

class gallery(models.Model):
    product=models.ForeignKey(productt,on_delete=models.CASCADE)
    images=models.FileField(upload_to='galleryDocs/')

class ga(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    details=models.EmailField(max_length=100)