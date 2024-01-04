from django.db import models

# Create your models here.
class District(models.Model):
    district_name=models.CharField(max_length=50)

    def __str__(self):
        return self.district_name


class Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name


class Brand(models.Model):
    brand_name=models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class helmetModels(models.Model):
    model_name=models.CharField(max_length=50)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Admintable(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.EmailField(unique=True,null=True)
    admin_password=models.CharField(max_length=50,unique=True)


class Complaint(models.Model):
    complaint_title=models.CharField(max_length=400)
    date=models.DateField(auto_now=True)
    user=models.IntegerField(default=0)
    seller=models.IntegerField(default=0)
    content=models.CharField(max_length=400)
    complaint_status=models.IntegerField(default=0)
    complaint_replay=models.CharField(max_length=99,default="not viewed yet")

class Feedback(models.Model):
    feedback=models.CharField(max_length=300)
    user=models.IntegerField(default=0)
    seller=models.IntegerField(default=0)