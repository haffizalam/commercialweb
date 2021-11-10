from django.shortcuts import render,redirect
from admin01.models import Category
from myshop.models import UserProfile
from .models import Product

# Create your views here.
def home(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	caobjs=Product.objects.all()
	
	cartobjs=Product.objects.filter(added_by_id=uobj.id)
	items=[]
	for i in cartobjs:
		items.append(i)

	return render(request,'sellerhome.html',{'items':items})


def add_product(request):
	catobj=Category.objects.all()
	if request.method=='POST':
		prdct_name=request.POST['proname']
		descr=request.POST['desc']
		mrkprice=request.POST['mprice']
		ourprice=request.POST['price']
		quant=request.POST['qty']
		image=request.FILES['image']
		catid=request.POST['ctg']

		cobj=Category.objects.get(id=catid)
		uobj=UserProfile.objects.get(user__username=request.user)

		pobj=Product(name=prdct_name,desc=descr,market_price=mrkprice,price=ourprice,quantityy=quant,product_img=image,category=cobj,added_by=uobj)
		pobj.save()

	return render(request, 'addproducts.html',{'catobj':catobj})


def delete_product(request,id):
	pobj=Product.objects.get(id=id)
	uobj=UserProfile.objects.get(user__username=request.user)
	c=Product.objects.get(added_by_id=uobj,id=id)
	c.delete()

	return redirect('/seller/home/')