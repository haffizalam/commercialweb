from django.shortcuts import render,redirect
from .models import Category
from myshop .models import UserProfile,User

# Create your views here.
def home(request):
	catobj=Category.objects.all()
	usobj=User.objects.all()
	ucnt=UserProfile.objects.all().count()
	seller=UserProfile.objects.filter(utype='Seller').count()
	buyer=UserProfile.objects.filter(utype='Buyer').count()
	admin=UserProfile.objects.filter(utype='Admin').count()
	return render(request,'adminhome.html',{'catobj':catobj,'usobj':usobj,'ucnt':ucnt,'seller':seller,'buyer':buyer,'admin':admin})

def add_category(request):

	if request.method == "POST":
		catname=request.POST['catname']
		caobj=Category(catname=catname)
		caobj.save()
		return redirect('/admin01/home/')
	return render(request,'adminhome.html')
def carousal_control(request):
	return render(request,'carousalhandle.html')
