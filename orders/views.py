import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem

# StripeのAPIキーを設定
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart_detail')

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        # Stripeで決済を作成
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                    'unit_amount': int(item.product.price * 100),  # 価格は「セント」単位
                },
                'quantity': item.quantity,
            } for item in cart_items],
            mode='payment',
            success_url=request.build_absolute_uri('/orders/success/'),
            cancel_url=request.build_absolute_uri('/orders/cancel/'),
        )
        return redirect(session.url)

    return render(request, 'orders/checkout.html', {'total_price': total_price})

def payment_success(request):
    return render(request, 'orders/success.html')

def payment_cancel(request):
    return render(request, 'orders/cancel.html')




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


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})
