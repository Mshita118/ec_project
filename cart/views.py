from django.shortcuts import redirect, get_object_or_404
from .models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')
