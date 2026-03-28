from django.db import models
from django.contrib.auth.models import User
from project.models import *
from datetime import date 
# Create your models here.

class Inquiry(models.Model):
    name       = models.CharField(max_length=50)
    email      = models.TextField()
    contact    = models.BigIntegerField()
    message    = models.TextField()
    created_At = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        db_table = 'inquiry'

# Feedback 
class Feedback(models.Model):
    rating     = models.CharField(max_length=15)
    message    = models.TextField()
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'feedback'        

class Profile(models.Model):
    contact  = models.BigIntegerField()
    user     = models.ForeignKey(User,on_delete=models.CASCADE)
    password = models.CharField(max_length=20,)

    class Meta():
        db_table = 'profile'  

class Cart(models.Model):
    product  = models.ForeignKey(Product,on_delete=models.CASCADE) 
    user     = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price    = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'cart'

class Order(models.Model):
    amount   = models.DecimalField(max_digits=10,decimal_places=2) 
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    date     = models.DateField(auto_now_add=True)
    status   = models.CharField(max_length=100)  

    class Meta:
        db_table = 'order'

class Order_details(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price    = models.DecimalField(max_digits = 10,decimal_places = 2)
    order    = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_details'

class Payment_Details(models.Model):
    order          = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=30)
    payment_id     = models.TextField()
    signature      = models.TextField()
    date           = models.DateField(auto_now=True)

    class Meta:
        db_table = 'payment_details' 

class Billing_detail(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    contact    = models.IntegerField()
    email      = models.CharField(max_length=50)
    address1   = models.TextField()
    city       = models.CharField(max_length=30)
    state      = models.CharField(max_length=30)
    pincode    = models.IntegerField()
    customer   = models.ForeignKey(User, on_delete=models.CASCADE)
    order      = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'billing_detail'

class Shipping_details(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

    class Meta:
        db_table = 'shipping_details'        