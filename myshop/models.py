from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	utype=models.CharField(max_length=20)
	mobile=models.CharField(max_length=11)

class D_Address(models.Model):
	user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	house_nm=models.CharField(max_length=20)
	street_nm=models.CharField(max_length=20)
	city_nm=models.CharField(max_length=20)
	state_nm=models.CharField(max_length=20)
	postal_code=models.IntegerField()