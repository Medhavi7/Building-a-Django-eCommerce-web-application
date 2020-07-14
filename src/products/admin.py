from django.contrib import admin

from .models import Product # we can even put products.models

class ProductAdmin(admin.ModelAdmin):
    list_display=['__str__', 'slug']
    class Meta:
        model=Product

admin.site.register(Product, ProductAdmin)