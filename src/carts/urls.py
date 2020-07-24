from django.conf.urls import url

app_name = 'cart'

from .views import (
    cart_home, 
    cart_update, 
    )


urlpatterns = [
    url('', cart_home, name='home'),
    url(r'update/', cart_update, name='update'),
]
