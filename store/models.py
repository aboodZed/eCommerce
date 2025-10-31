from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    details = models.TextField()
    qty = models.IntegerField(default=0)
    price = models.FloatField(default=1.0)
    
class Cart(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    
class Order(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)
    status = models.CharField(max_length=100, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
