from django.urls import path
from . import views

app_name = "admin01"

urlpatterns = [
	path('home/', views.home),
	path('add_category/',views.add_category,name='add_category'),
	path('carousal_control/',views.carousal_control)
]