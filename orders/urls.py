from django.urls import path
from .views import place_order, order_list


urlpatterns = [
    path('place/', place_order, name='place_order'),
    path('list/', order_list, name='order_list')
]
