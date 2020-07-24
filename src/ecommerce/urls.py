from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView



from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    
    url('admin/', admin.site.urls),
    url('about/', about_page, name='about'),
    url('contact/', contact_page, name='contact'),
    url('login/', login_page, name='login'),
    url('cart/', include("carts.urls", namespace='cart')),
    url('register/', register_page, name='register'),
    url('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    url('products/', include("products.urls", namespace='products')),
    url('search/', include("search.urls", namespace='search')),
    url('', home_page, name='home'),
    
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)