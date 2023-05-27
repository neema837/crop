from django.db import models
from farmer.models import *
from django.utils import timezone
# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=20)
    lname=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    locality=models.CharField(max_length=20,null=True,blank=True)
    adtype=models.CharField(max_length=10,null=True,blank=True)
    state=models.CharField(max_length=15,null=True,blank=True)
    zipcode=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    cusid=models.ForeignKey(customer,on_delete=models.CASCADE)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    farmid=models.ForeignKey(Registeration,on_delete=models.CASCADE,null=True,blank=True)
    qty=models.IntegerField()
    subtotal=models.IntegerField(null=True)
    created_at=models.DateField(default=timezone.now)
    paystatus=models.BooleanField(default=False)

class Orders(models.Model):
    cusid=models.ForeignKey(customer,on_delete=models.CASCADE)
    cartid=models.ManyToManyField(Cart)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    locality=models.CharField(max_length=20)
    adtype=models.CharField(max_length=10)
    state=models.CharField(max_length=15)
    zipcode=models.CharField(max_length=10)
    created_at=models.DateField(default=timezone.now)
    paystatus=models.BooleanField(default=False)
    approval=models.BooleanField(default=False)
    
class wishlist(models.Model):
    cusid=models.ForeignKey(customer,on_delete=models.CASCADE)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    farmid=models.ForeignKey(Registeration,on_delete=models.CASCADE)