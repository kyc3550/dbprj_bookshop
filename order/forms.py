from django import forms

from .models import Order

    
class OrderCreateForm(forms.ModelForm):
    post_code = forms.CharField(label='우편번호')
    customer_name = forms.CharField(label='주문자이름')
    base_address = forms.CharField(label='기본주소')
    detail_address = forms.CharField(label='상세주소')
   
    class Meta:
        model = Order
        fields = ['customer_name','email','post_code','base_address','detail_address']