from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# ... (другие представления)

def index(request):
    """Отображает главную страницу с товарами."""
    products = Product.objects.all()
    categories = Category.objects.all()  # Получаем все категории
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/index.html', context)

def product_list(request, category_slug=None):
    """
    Отображает список товаров.
    """
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()  # Получаем все категории

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'products': products,
        'category': category,
        'categories': categories
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request):
    """Отображает главную страницу с товарами."""
    products = Product.objects.all()
    categories = Category.objects.all()  # Получаем все категории
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/product_detail.html', context)

def product_list_by_category(request):
    """Отображает главную страницу с товарами."""
    products = Product.objects.all()
    categories = Category.objects.all()  # Получаем все категории
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/product_list_by_category.html', context)