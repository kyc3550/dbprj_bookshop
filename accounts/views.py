from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,AddressForm,CardForm
from .models import Address2,Card
from django.contrib.auth.models import User
from django.views import View
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

class ProfileUpdateView(View): # 간단한 View클래스를 상속 받았으므로 get함수와 post함수를 각각 만들어줘야한다.
    # 프로필 편집에서 보여주기위한 get 메소드
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)  # 로그인중인 사용자 객체를 얻어옴
        user_form = RegisterForm(initial={
            'username': user.username,
        })

        if hasattr(user, 'card'):  # user가 profile을 가지고 있으면 True, 없으면 False (회원가입을 한다고 profile을 가지고 있진 않으므로)
            card_profile = user.card
            card_profile_form = CardForm(initial={
                'card_num' : card_profile.card_num,
                'card_expirantion' : card_profile.card_expirantion,
                'card_choice' : card_profile.card_choice,
            })
        else:
            card_profile_form = CardForm()

        if hasattr(user, 'address2'):  # user가 profile을 가지고 있으면 True, 없으면 False (회원가입을 한다고 profile을 가지고 있진 않으므로)
            address_profile = user.address2
            address_profile_form = AddressForm(initial={
                'post_code' : address_profile.post_code,
                'user_name' : address_profile.user_name,
                'base_address' : address_profile.base_address,
                'detail_address' : address_profile.detail_address,
            })
        else:
            address_profile_form = Address2()

        return render(request, 'registration/profile_update.html', {"user_form": user_form, "card_profile_form": card_profile_form,'address_profile_form':address_profile_form})

    def post(self, request):
        u = User.objects.get(id=request.user.pk)        # 로그인중인 사용자 객체를 얻어옴
        user_form = RegisterForm(request.POST, instance=u)  # 기존의 것의 업데이트하는 것 이므로 기존의 인스턴스를 넘겨줘야한다. 기존의 것을 가져와 수정하는 것

        # User 폼
        if user_form.is_valid():
            user_form.save()

        if hasattr(u, 'user'):
            profile = u.user
            profile_form = RegisterForm(request.POST, instance=profile) # 기존의 것 가져와 수정하는 것
        else:
            profile_form = RegisterForm(request.POST) # 새로 만드는 것

        # Profile 폼
        if profile_form.is_valid():
            card_profile = profile_form.save(commit=False) # 기존의 것을 가져와 수정하는 경우가 아닌 새로 만든 경우 user를 지정해줘야 하므로
            address2_profile = profile_form.save(commit=False)
            card_profile.user = u
            address2_profile.user = u
            card_profile.save()
            address2_profile.save()
        return redirect('/', pk=request.user.pk) # 수정된 화면 보여주기

    