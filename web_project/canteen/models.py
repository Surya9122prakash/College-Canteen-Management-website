from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menus(models.Model):
    sno=models.IntegerField(default=1)
    name=models.CharField(max_length=50,null=True)
    id=models.CharField(max_length=35,null=False,primary_key=True)
    price=models.CharField(max_length=35,null=True)
    thumbnail=models.ImageField(upload_to="files/thumbnail", null=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    price=models.CharField(max_length=35,null=True)
    quantity=models.IntegerField(default=1)
    order_confirmed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name