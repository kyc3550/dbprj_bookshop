  
from django.shortcuts import render, get_object_or_404
from .models import *
from cart.views import cart_detail,cart_item_find
from .forms import *

def order_create(request):
    
    cart = cart_item_find(request)
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for cart_item in cart:
                OrderItem.objects.create(order=order, product=cart_item.product, price=cart_item.product.book_price, quantity=cart_item.quantity)
            
            return render(request, 'order/created.html', {'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart':cart, 'form':form})

    # ajax로 결제 후에 보여줄 결제 완료 화면
def order_complete(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    return render(request,'order/created.html',{'order':order})

# 결제를 위한 임포트
from django.views.generic.base import View
from django.http import JsonResponse

class OrderCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"로그인을 해주세요":False}, status=403)
        
        cart = cart_item_find(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for cart_item in cart:
                OrderItem.objects.create(order=order, product=cart_item.product, price=cart_item.product.book_price, quantity=cart_item.quantity)
            data = {
                "order_id": order.id
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)

# 결제 정보 생성
class OrderCheckoutAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated":False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        amount = request.POST.get('amount')

        try:
            merchant_order_id = OrderTransaction.objects.create_new(
                order=order,
                amount=amount
            )
        except:
            merchant_order_id = None


        if merchant_order_id is not None:
            data = {
                "works": True,
                "merchant_id": merchant_order_id
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)

# 실제 결제가 이뤄진 것이 있는지 확인
class OrderImpAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated":False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        merchant_id = request.POST.get('merchant_id')
        imp_id = request.POST.get('imp_id')
        amount = request.POST.get('amount')

        try:
            trans = OrderTransaction.objects.get(
                order=order,
                merchant_order_id=merchant_id,
                amount=amount
            )
        except:
            trans = None

        if trans is not None:
            trans.transaction_id = imp_id
            trans.success = True
            trans.save()
            order.paid = True
            order.save()

            data = {
                "works": True
            }

            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)