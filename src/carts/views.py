from django.shortcuts import render

from .models import Cart

def cart_home(request):
	request.session['cart_id'] = "abc"
	cart_id = request.session.get("cart_id", None)
	if cart_id is None:
		cart_obj = Cart.objects.create(user=None)
		request.session['cart_id'] = cart_obj.id
		print('New Cart created')
	else:
		print('Cart ID exists')
		print(cart_id)
		cart_obj = Cart.objects.get(id=cart_id)
	return render(request, "carts/home.html", {})
