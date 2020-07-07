from django.contrib import admin

from .models import Product # we can even put products.models

admin.site.register(Product)