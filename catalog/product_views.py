from django.shortcuts import render, get_object_or_404

from .models import Product  # Импортируйте модель товара

def product_detail(request, pk):
    """
    Отображает страницу с деталями товара.
    """
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)