from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'category'

class Subcategory(models.Model):
    subcategory = models.CharField(max_length=50,default='')
    name = models.ForeignKey(Category,on_delete=models.CASCADE,default='')

    class Meta:
        db_table = 'subcategory'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    small_des = models.TextField(max_length=150)
    large_des = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)

    class Meta:
        db_table = 'product'                
	
class State(models.Model):
    state = models.CharField(max_length=50)

    class Meta:
        db_table = 'state'

class City(models.Model):
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'  

class Area(models.Model):
    area = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta():
        db_table = 'Area'              		