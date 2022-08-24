from django.db import models

# Create your models here.
class registerdata(models.Model):
    uname=models.CharField(max_length=50,primary_key="true")
    mnumber=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    Password=models.CharField(max_length=50)

class servicedetail(models.Model):
    uname=models.CharField(max_length=50,null="true")
    date=models.DateField(auto_now=False, auto_now_add=False,null="true")
    servicedel=models.CharField(max_length=150,null="true")
    vname=models.CharField( max_length=50,null="true")
    vnumber=models.CharField( max_length=50,null="true")
    vtype=models.CharField(max_length=100,null="true")
    flag=models.IntegerField(null="true")

class ownermain(models.Model):
    main=models.CharField( max_length=150)
    adout=models.TextField()

class adminlog(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
class adminvalid(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
class delivery(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=100)
    flag=models.IntegerField()
