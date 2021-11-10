"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('search1/',views.search1,name='search1'),
    path('signup_call/',views.signup_call,name='signup_call'),
    path('login_call/',views.login_call,name='login_call'),
    path('add_address/',views.add_address,name='add_address'),
    path('logout_call/',views.logout_call),
    path('seller/',include('seller.urls')),
    path('buyer/',include('buyer.urls')),
    path('admin01/',include('admin01.urls'))
    


]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
