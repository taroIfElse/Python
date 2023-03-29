from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.product_set.all()
    return render(request, 'store/category_detail.html', {'category': category, 'products': products})
