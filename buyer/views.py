from django.shortcuts import render,redirect
from seller.models import Product
from myshop.models import UserProfile,D_Address
from .models import Cart,wishlist

# Create your views here.

def home(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	pobjs=Product.objects.all()
	caobjs=Cart.objects.all()
	count=Cart.objects.filter(user_id=uobj.id).count()
	wcnt=wishlist.objects.filter(user_id=uobj.id).count()
	cartobjs=Cart.objects.filter(user_id=uobj.id)
	items=[]
	print(count)
	for i in cartobjs:
		items.append(Product.objects.get(id=i.product_id))
	return render(request,'buyerhome.html',{'pobjs':pobjs,'cnt':count,'wcnt':wcnt,'items':items})

def mycart(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	caobjs=Cart.objects.all()
	count=Cart.objects.filter(user_id=uobj.id).count()
	cartobjs=Cart.objects.filter(user_id=uobj.id)
	items=[]
	for i in cartobjs:
		items.append(Product.objects.get(id=i.product_id))
	return render(request,'mycart.html',{'items':items,'cnt':count})
def mywishlist(request):
	usobj=UserProfile.objects.get(user__username=request.user)
	wcnt=wishlist.objects.filter(user_id=usobj.id).count()
	wobjs=wishlist.objects.filter(user_id=usobj.id)
	wlist=[]
	for i in wobjs:
		wlist.append(Product.objects.get(id=i.product_id))
	return render(request,'wishlist.html',{'wlist':wlist,'wcnt':wcnt})

def add_cart(request,id):
	try:
		pobj=Product.objects.get(id=id)
		uobj=UserProfile.objects.get(user__username=request.user)

		c=Cart(product=pobj,user=uobj)
		c.save()
		return redirect('/buyer/home/')

	except:
		return redirect('/buyer/home/')

	
def add_wishlist(request,id):
	try:
		pobj=Product.objects.get(id=id)
		uobj=UserProfile.objects.get(user__username=request.user)

		w=wishlist(product=pobj,user=uobj)
		w.save()
		return redirect('/buyer/home/')

	except:
		return redirect('/buyer/home/')

def del_cart(request,id):
	pobj=Product.objects.get(id=id)
	uobj=UserProfile.objects.get(user__username=request.user)
	c=Cart.objects.get(user=uobj,product=pobj)
	c.delete()

	return redirect('/buyer/mycart/')
def del_wishlist(request,id):
	pobj=Product.objects.get(id=id)
	uobj=UserProfile.objects.get(user__username=request.user)
	w=wishlist.objects.get(user=uobj,product=pobj)
	w.delete()

	return redirect('/buyer/mywishlist/')

def placeorder(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	caobjs=Cart.objects.all()
	count=Cart.objects.filter(user_id=uobj.id).count()
	addrobj=D_Address.objects.filter(user_id=uobj)
	addrs=[]
	pradrs=[]
	for i in addrobj:
		addrs.append(i)
	pradrs.append(addrs[0])
	print(pradrs)
	return render(request,'placeorder.html',{'addrs':pradrs,'cnt':count})
