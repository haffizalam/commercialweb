from django.db import models
from myshop.models import UserProfile
from admin01.models import Category


# Create your models here.


class Product(models.Model):
	name= models.CharField(max_length=100)
	desc= models.CharField(max_length=200)
	market_price=models.DecimalField(decimal_places=2,max_digits=12)
	price= models.DecimalField(decimal_places=2, max_digits=12)
	quantityy= models.IntegerField()
	product_img=models.ImageField(upload_to="product_image",blank=True)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	added_by=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now=True)
	
	

