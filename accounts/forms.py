from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=30,label='이름')
    username = forms.CharField(max_length=30,label='아이디(회원번호)')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재입력',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username',]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 다릅니다.')
        return cd['password2']

#class RegisterForm_Address(forms.ModelForm):
