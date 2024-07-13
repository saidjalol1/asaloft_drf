from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Product, Category, ColorImages, Order, ProductImages
from .serializers import ProductSerializer, CategorySerializer, ColorImagesSerializer, OrderCreateSerializer
from .telegram_bot_utils import send_order_notification

class ColorImagesListAPIView(generics.ListAPIView):
    queryset = ColorImages.objects.all()
    serializer_class = ColorImagesSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category__id=category_id)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
    
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        instance = serializer.save()
        send_order_notification(instance)