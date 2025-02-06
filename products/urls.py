from django.urls import path
from .views import add_product, product_list
from . import views

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),
]
