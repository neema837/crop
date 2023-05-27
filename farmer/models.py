from django.db import models

# Create your models here.
class Registeration(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    cname=models.CharField(max_length=20)
    cimage=models.FileField(upload_to="users")
    farmid=models.ForeignKey(Registeration,on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

class Product(models.Model):
    pname=models.CharField(max_length=20)
    des=models.CharField(max_length=50)
    price=models.IntegerField()
    pimage=models.FileField(upload_to="users")
    catid=models.ForeignKey(Category,on_delete=models.CASCADE)
    farmid=models.ForeignKey(Registeration,on_delete=models.CASCADE)
    stock=models.IntegerField(null=True,blank=True)
    unit=models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return self.pname


class Blog(models.Model):
    categ=models.CharField(max_length=20)
    bdes=models.CharField(max_length=50)
    bimage=models.FileField(upload_to="users")
    farmid=models.ForeignKey(Registeration,on_delete=models.CASCADE)

class Skill(models.Model):
    scat=models.CharField(max_length=20)
    sdes=models.CharField(max_length=50)
    simage=models.FileField(upload_to="users")
    farmid=models.ForeignKey(Registeration,on_delete=models.CASCADE)