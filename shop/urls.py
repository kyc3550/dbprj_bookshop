from django.urls import path
from .views import *
app_name = 'shop' #get_absoluteurl 사용 위함

urlpatterns = [
    path('',book_list, name='product_all'),
    path('<int:book_num>/',product_detail,name = 'product_detail')
]
