from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "shop_app"

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/category/<int:category_id>/', views.ProductByCategoryAPIView.as_view(), name='product-by-category'),
    path('orders/create/', views.OrderCreateAPIView.as_view(), name='order-create'),
    
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('color_images/', views.ColorImagesListAPIView.as_view(), name='product-detail'),
]