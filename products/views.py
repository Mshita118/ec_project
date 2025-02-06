from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
