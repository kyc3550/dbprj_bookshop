from django.contrib import admin
from .models import Address2,Card
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','user_name', 'post_code', 'base_address', 'detail_address']

admin.site.register(Address2,AddressAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ['user','card_num', 'card_expirantion', 'card_choice']
admin.site.register(Card,CardAdmin)
'''
class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False
    verbose_name = 'Address'
    fk_name='user'

class CustomUserAdmin(UserAdmin):
    inlines = (AddressInline,)

    def get_inline_instances(self,request,obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request,obj)

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
'''