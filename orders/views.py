from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem


@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart_detail')

    total_price = sum(item.product.price *
                      item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)

    for item in cart_items:
        OrderItem.objects.create(
            order=order, product=item.product, quantity=item.quantity)

    cart_items.delete()

    return redirect('order_list')


@login_required
def order_list(request):
    orders = Order.objects.filter(
        user=request.user).prefetch_related('items__product')
    return render(request, 'orders/order_list.html', {'orders': orders})
