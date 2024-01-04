from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class Booking(models.Model):
    user=models.ForeignKey(newuser,on_delete=models.CASCADE)
    booking_status=models.IntegerField(default=0)
    booking_date=models.DateField(auto_now_add=True)

class Cart(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    product=models.ForeignKey("Seller.productt",on_delete=models.CASCADE)
    booking_quantity=models.IntegerField(default=1)





