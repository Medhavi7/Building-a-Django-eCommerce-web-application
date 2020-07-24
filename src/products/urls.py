
from django.conf.urls import url

app_name = 'products'

from .views import (
    ProductListView, 
    ProductDetailSlugView, 
    )


urlpatterns = [
    url('', ProductListView.as_view(), name='list'),
    url(r'(?P<slug>[\w-]+)', ProductDetailSlugView.as_view(), name='detail'),
]


