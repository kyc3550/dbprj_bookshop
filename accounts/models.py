from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Address2(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,max_length=10)
    user_name = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    base_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name



class Card(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,max_length=10)
    card_num = models.CharField(max_length=20)
    card_expirantion = models.DateField()
    card_choice = models.CharField(max_length=10)
        
'''   
@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        Address.objects.create(user=instance)
    instance.profile.save()
'''