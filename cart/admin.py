from django.contrib import admin
from .models import CartItem
# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product','cart','quantity',]
admin.site.register(CartItem, CartItemAdmin)