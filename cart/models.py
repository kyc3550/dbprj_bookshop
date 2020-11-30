from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    objects = models.Manager()
    cart_id = models.CharField(max_length=250,primary_key=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    objects = models.Manager()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.book_price * self.quantity

    def __str__(self):
        return str(self.product)

    