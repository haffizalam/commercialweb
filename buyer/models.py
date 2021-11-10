from django.db import models
from myshop.models import UserProfile
from seller.models import Product

# Create your models here.
class Cart(models.Model):

	#composite unique key
	class Meta():
		unique_together=('user','product')

	user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)

class wishlist(models.Model):

	#composite unique key
	class Meta():
		unique_together=('user','product')

	user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)


