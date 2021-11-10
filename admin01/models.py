from django.db import models
from myshop.models import UserProfile


# Create your models here.
class Category(models.Model):
	catname=models.CharField(max_length=50)


