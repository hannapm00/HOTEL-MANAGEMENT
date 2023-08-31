from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class chef(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    number=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    experiance=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.name        


class staff(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    number=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    experiance=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.name


    
class reservation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20) 
    fordate=models.CharField(max_length=20)
    fromtime=models.CharField(max_length=10)
    totime=models.CharField(max_length=10)
    num=models.IntegerField()
    tablemembers=models.IntegerField()
    address=models.CharField(max_length=10) 
    status=models.CharField(max_length=10)    

    def __str__(self):
        return self.name        

class outsideuser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    num=models.IntegerField() 
    address=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20) 
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=10)    