from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile,D_Address
from django.contrib.auth import authenticate, login, logout
from seller.models import Product
from admin01 .models import Category
def index(request):
	
	pobjs=Product.objects.all()
	catobj=Category.objects.all()
	
	s1obj=(pobjs[0:3])
	s2obj=(pobjs[3:6])
	s3obj=(pobjs[6:9])

	
	
	return render(request,'index.html',{'pobjs':pobjs,'s1obj':s1obj,'s2obj':s2obj,'s3obj':s3obj,'catobj':catobj})

def signup_call(request):
	if request.method=='POST':
		fn=request.POST['fname']
		ln=request.POST['lname']
		un=request.POST['uname']
		passwd=request.POST['pwd']
		mail=request.POST['email']
		usrtype=request.POST['ustype']
		mob=request.POST['mobileno']

		
		userobj=User(first_name=fn,last_name=ln,username=un,password=make_password(passwd),email=mail)
		userobj.save()

		uprofileobj=UserProfile(user=userobj,utype=usrtype,mobile=mob)
		uprofileobj.save()
		
		return redirect('/index/')
	return render(request,'index.html')

def login_call(request):
	if request.method=='POST':
		usernm=request.POST['usrname']
		passwd=request.POST['pwd']

		user=authenticate(username=usernm,password=passwd)
		if user:
			login(request,user)
			profileobj=UserProfile.objects.get(user__username=request.user)
			if profileobj.utype=='Admin':
				return redirect('/admin01/home/')
			elif profileobj.utype== 'Seller':
				print('seller')
				return redirect('/seller/home/')
			else:
				return redirect('/buyer/home')
				print('buyer')
		else:
			return HttpResponse("<h1>Invalid Credentials</h1>")

def search1(request):
	s=[]
	catobj=Category.objects.all()
	prd=Product.objects.all()
	if request.method=='POST':
		keyword=request.POST['item']
	print(keyword)
	for i in prd:
		if keyword.lower() in i.name or keyword.capitalize() in i.name:
			s.append(i)
	return render(request,'search.html',{'catobj':catobj,'s':s})
        

def add_address(request):
	
	if request.method=='POST':
		hse=request.POST['house']
		strt=request.POST['street']
		citynm=request.POST['city']
		statenm=request.POST['state']
		postal=request.POST['pin']

		profileobj=UserProfile.objects.get(user__username=request.user)

		addobj=D_Address(user=profileobj,house_nm=hse,street_nm=strt,city_nm=citynm,state_nm=statenm,postal_code=postal)
		addobj.save()


	return render(request,'placeorder.html')

def logout_call(request):
	logout(request)
	return redirect('/index/')