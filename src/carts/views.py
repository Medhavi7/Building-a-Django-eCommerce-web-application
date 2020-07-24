from django.shortcuts import render

from products.models import Product
from .models import Cart


def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	# print(cart_obj)	
	products = cart_obj.products.all()
	total = 0
	print(products)
	for x in products:
		print(x)
		total = total + x.price
	print(total)
	cart_obj.total = total
	cart_obj.save()
	return render(request, "carts/home.html", {})

def cart_update(request):
	obj = Product.objects.get(id=1)
	return