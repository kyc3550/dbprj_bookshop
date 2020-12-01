from django import forms

from .models import Order
CARD_CHOICE = (
    ('KB','국민카드'),
    ('SinHan','신한카드'),
    ('Samsung','삼성카드'),
    ('IBK','기업은행'),
    ('KAKAO','카카오뱅크'),
    ('BC','비씨카드'),
    ('LOTTE','롯데카드')
)

    
class OrderCreateForm(forms.ModelForm):
    post_code = forms.CharField(label='우편번호')
    customer_name = forms.CharField(label='주문자이름')
    base_address = forms.CharField(label='기본주소')
    detail_address = forms.CharField(label='상세주소')
    card_num = forms.CharField(label='카드번호')
    card_expirantion = forms.DateField(label='유효기간(YYYY-MM-DD)')
    card_choice = forms.ChoiceField(label='카드종류',choices=CARD_CHOICE)
    class Meta:
        model = Order
        fields = ['customer_name','email','card_expirantion','card_choice','post_code','base_address','detail_address']