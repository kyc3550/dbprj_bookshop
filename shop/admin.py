from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['book_num','book_name','book_stock','book_price','created','updated']
    list_editable = ['book_price','book_stock']
admin.site.register(Product,ProductAdmin)