from django.db import models

# Create your models here.
class ExpFarmer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    password=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=50)
    approve=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
