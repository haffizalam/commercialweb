from django.urls import path
from . import views

app_name = "buyer"

urlpatterns = [
	path('home/', views.home),
	path('add_cart/<int:id>/',views.add_cart,name='add_cart'),
	path('add_wishlist/<int:id>/',views.add_wishlist,name='add_wishlist'),
	path('del_cart/<int:id>/',views.del_cart,name='del_cart'),
	path('del_wishlist/<int:id>/',views.del_wishlist,name='del_wishlist'),
	path('placeorder/',views.placeorder,name='placeorder'),
	#path('add_address/',views.add_address,name='add_address'),
	path('mycart/',views.mycart),
	path('mywishlist/',views.mywishlist,name='mywishlist')
	#path('add_product/',views.add_product),
	#path('add_category/',views.add_category)
]