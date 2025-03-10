from django.urls import path
from .views import add_product, product_list, product_detail
from . import views

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
