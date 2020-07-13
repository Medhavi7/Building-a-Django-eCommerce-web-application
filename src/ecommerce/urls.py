"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import url

from products.views import (
    ProductListView, 
    product_list_view, 
    ProductDetailView, 
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView
    )

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    
    url('admin/', admin.site.urls),
    url('about/', about_page),
    url('contact/', contact_page),
    url('login/', login_page),
    url('register/', register_page),
    url('featured/', ProductFeaturedListView.as_view()),
    url(r'featured/(?P<pk>\d+)', ProductFeaturedDetailView.as_view()),
    url('products/', ProductListView.as_view()),
    url('products-fbv/', product_list_view),
    url(r'products/(?P<pk>\d+)', ProductDetailView.as_view()),
    url(r'products-fbv/(?P<pk>\d+)', product_detail_view),
    url('', home_page),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)