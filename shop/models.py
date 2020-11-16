from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    book_num = models.IntegerField(unique=True,db_index=True)
    book_name = models.CharField(max_length=30,db_index=True)
    book_stock = models.IntegerField()
    book_price = models.DecimalField(max_digits=10, decimal_places=2) # max_digits, decimal_place 달러(등 해외단위) 단위를 위함.
    
    #여기서 부터 선택적
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-created',)  #정렬기준

    def __str__(self):
        return self.book_name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.book_num])
        