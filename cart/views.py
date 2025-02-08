from django.shortcuts import redirect, get_object_or_404, render
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


@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price *
                      item.quantity for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_detail')
