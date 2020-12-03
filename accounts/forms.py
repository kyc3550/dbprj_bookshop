from django.contrib.auth.models import User
from .models import Address2,Card
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='회원번호(ID)',help_text=False)
    password = forms.CharField(label='비밀번호',widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재입력',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username',]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 다릅니다.')
        return cd['password2']

class AddressForm(forms.ModelForm):
    post_code = forms.CharField(label='우편번호')
    user_name = forms.CharField(label='이름')
    base_address = forms.CharField(label='기본주소')
    detail_address = forms.CharField(label='상세주소')
    class Meta:
        model = Address2
        fields = ['user_name', 'post_code', 'base_address', 'detail_address']  

CARD_CHOICE = (
    ('KB','국민카드'),
    ('SinHan','신한카드'),
    ('Samsung','삼성카드'),
    ('IBK','기업은행'),
    ('KAKAO','카카오뱅크'),
    ('BC','비씨카드'),
    ('LOTTE','롯데카드')
)
class CardForm(forms.ModelForm):
    card_num = forms.CharField(label='카드번호')
    card_expirantion = forms.DateField(label='유효기간(YYYY-MM-DD)')
    card_choice = forms.ChoiceField(label='카드종류',choices=CARD_CHOICE)
    class Meta:
        model = Card
        fields = ['card_num', 'card_expirantion', 'card_choice']    

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields= ['username']