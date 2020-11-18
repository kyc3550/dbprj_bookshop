from django.shortcuts import render
from .forms import RegisterForm,AddressForm,CardForm
from .models import Address2,Card
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