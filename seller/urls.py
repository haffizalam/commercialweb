from django.urls import path
from . import views

app_name = "seller"

urlpatterns = [
	path('home/', views.home),
	path('add_product/',views.add_product),
	path('delete_product/<int:id>/',views.delete_product,name='delete_product')
	
]