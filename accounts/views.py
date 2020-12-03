from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,AddressForm,CardForm,CustomUserChangeForm
from .models import Address2,Card
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
def register(request):
    if request.method == 'POST':
          #회원가입 데이터 입력 완료
        user_form = RegisterForm(request.POST)
        address_form = AddressForm(request.POST)
        card_form = CardForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_address = Address2(
                user = new_user,
                post_code = request.POST['post_code'],
                user_name = request.POST['user_name'],
                base_address = request.POST['base_address'],
                detail_address = request.POST['detail_address'],
            )
            new_card = Card(
                user = new_user,
                card_num = request.POST['card_num'],
                card_expirantion = request.POST['card_expirantion'],
                card_choice = request.POST['card_choice'],
            )
            new_address.save()
            new_card.save()

            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        #회원가입 내용을 입력하는 상황
        user_form = RegisterForm()
        address_form = AddressForm()
        card_form = CardForm()

    return render(request, 'registration/register.html',{
        'user_form':user_form,
        'address_form':address_form,
        'card_form':card_form})

class ProfileUpdateView(View): 
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk) 
        '''
        user_form = RegisterForm(initial={
            'username': user.username,
        })
        '''
        user_change_form = CustomUserChangeForm(instance=request.user)
        context = {
            'user_change_form' : user_change_form,
        }
        if hasattr(user, 'card'):  
            card_profile = user.card
            card_profile_form = CardForm(initial={
                'card_num' : card_profile.card_num,
                'card_expirantion' : card_profile.card_expirantion,
                'card_choice' : card_profile.card_choice,
            })
        else:
            card_profile_form = CardForm()

        if hasattr(user, 'address2'): 
            address_profile = user.address2
            address_profile_form = AddressForm(initial={
                'post_code' : address_profile.post_code,
                'user_name' : address_profile.user_name,
                'base_address' : address_profile.base_address,
                'detail_address' : address_profile.detail_address,
            })
        else:
            address_profile_form = Address2()
        return render(request, 'registration/profile_update.html', { 'user_change_form':user_change_form,'card_profile_form': card_profile_form,'address_profile_form':address_profile_form})

    def post(self, request):
        u = User.objects.get(id=request.user.pk)     
        #user_form = RegisterForm(request.POST, instance=u)
        user_change_form = CustomUserChangeForm(data=request.POST,instance=u)
        
        card_profile = u.card
        card_profile_form = CardForm(request.POST,instance=card_profile)

        address_profile = u.address2
        address_profile_form = AddressForm(request.POST,instance=address_profile)

        # User 폼
        if user_change_form.is_valid():
            user_change_form.save()
            card_profile_form.save()
            address_profile_form.save()

        return render(request, 'registration/profile_update.html', {"user_change_form": user_change_form, "card_profile_form": card_profile_form,'address_profile_form':address_profile_form})
    
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST,)
        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request,request.user)
            return redirect('/')
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'registration/password.html',{'password_change_form':password_change_form})
    
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'registration/delete.html')