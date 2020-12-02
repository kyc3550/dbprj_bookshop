from django.contrib import admin

# Register your models here.
from .models import OrderItem, Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name','email','post_code','base_address','detail_address','paid','created','updated']
    list_filter = ['paid','created','updated']
    inlines = [OrderItemInline]
admin.site.register(Order, OrderAdmin)
