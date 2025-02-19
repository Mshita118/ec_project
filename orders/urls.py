from django.urls import path
from .views import place_order, order_list, checkout, payment_success, payment_cancel, order_history


urlpatterns = [
    path('place/', place_order, name='place_order'),
    path('list/', order_list, name='order_list'),
    path('checkout/', checkout, name='checkout'),
    path('success/', payment_success, name='payment_success'),
    path('cancel/', payment_cancel, name='payment_cancel'),
    path('history/', order_history, name='order_history'),
]
