from django.shortcuts import render, get_object_or_404
from .models import Product

def product_view(request, product_id):
    """
    Отображает страницу с информацией о конкретном продукте.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'product/product_view.html', context)