"""nextgen URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from store.views import home, about, contact, services, shop, details, subcategory, form
from store.views import login, logout
from blog.views import blog, blogdetails, blogcategories


urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^$', home, name='home'),
     url(r'^index', home, name='home'),
     url(r'^quotationreq', form, name='form'),
     path('subcategory/<id>', subcategory, name='subcategory'),
     url(r'^about', about, name='about'),
     url(r'^contact', contact, name='contact'),
     url(r'^services', services, name='services'),  
     url(r'^shop', shop, name='shop'),     
     url(r'^login/', login, name='login'),
     url(r'^logout/', logout, name='logout'),
     url(r'^blog/', blog, name='blog'),
     path('blogdetails/<id>', blogdetails, name='blogdetails'),
     path('blogcategories/<id>', blogcategories, name='blogcategories'),
     path('product/details/<id>', details, name='details' ),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)