from django.contrib import admin
from .models import Address2,Card
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
'''
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','user_name', 'post_code', 'base_address', 'detail_address']

admin.site.register(Address2,AddressAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ['user','card_num', 'card_expirantion', 'card_choice']
admin.site.register(Card,CardAdmin)

'''
class AddressAdmin(admin.StackedInline):
    model = Address2
    con_delete = False

class CardAdmin(admin.StackedInline):
    model = Card
    con_delete = False
    
class CustomUserAdmin(UserAdmin):
    inlines = (CardAdmin,AddressAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
