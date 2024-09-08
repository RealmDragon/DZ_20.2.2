from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('products/', views.product_list, name='product_list'),  # Список товаров
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Детальная страница товара
    path('product/<int:product_id>/', views.product_view, name='product_view'),
    path('products/category/<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),  # Список товаров по категории
]