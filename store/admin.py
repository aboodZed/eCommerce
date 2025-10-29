from django.contrib import admin
from .models import Product, Cart, Order, OrderItem
# Register your models here.

admin.site.register([Product, Cart, Order, OrderItem])